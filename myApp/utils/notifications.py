import requests
from datetime import timedelta
from django.conf import settings
from django.utils import timezone
from django.db.models import Avg

from myApp.models import (
    CourseEnrollment,
    EmailNotificationLog,
    ExamAttempt,
    ExamResultSummary,
    TrainingReminder,
    UserProgress,
)


def send_resend_email(subject, html, to_email, notification_type, recipient_user=None, related_course=None, related_exam_attempt=None):
    log = EmailNotificationLog.objects.create(
        recipient_user=recipient_user,
        recipient_email=to_email,
        notification_type=notification_type,
        subject=subject,
        body=html,
        status='queued',
        related_course=related_course,
        related_exam_attempt=related_exam_attempt,
    )

    api_key = getattr(settings, 'RESEND_API_KEY', '')
    from_email = getattr(settings, 'RESEND_FROM_EMAIL', '')
    if not api_key or not from_email:
        log.status = 'failed'
        log.error_message = 'Missing RESEND_API_KEY or RESEND_FROM_EMAIL in environment.'
        log.save(update_fields=['status', 'error_message'])
        return False, None

    try:
        response = requests.post(
            'https://api.resend.com/emails',
            headers={
                'Authorization': f'Bearer {api_key}',
                'Content-Type': 'application/json',
            },
            json={
                'from': from_email,
                'to': [to_email],
                'subject': subject,
                'html': html,
            },
            timeout=30,
        )
        if response.status_code in (200, 201):
            data = response.json()
            log.status = 'sent'
            log.sent_at = timezone.now()
            log.provider_message_id = data.get('id', '')
            log.save(update_fields=['status', 'sent_at', 'provider_message_id'])
            return True, data.get('id')
        log.status = 'failed'
        log.error_message = f'{response.status_code}: {response.text[:500]}'
        log.save(update_fields=['status', 'error_message'])
        return False, None
    except Exception as exc:
        log.status = 'failed'
        log.error_message = str(exc)
        log.save(update_fields=['status', 'error_message'])
        return False, None


def upsert_exam_result_summary(exam_attempt):
    exam = exam_attempt.exam
    course = exam.course
    user = exam_attempt.user
    total_trainings = course.lessons.count()
    completed_trainings = UserProgress.objects.filter(user=user, lesson__course=course, completed=True).count()
    avg_watch = UserProgress.objects.filter(user=user, lesson__course=course).aggregate(avg=Avg('video_watch_percentage'))['avg'] or 0
    summary_text = (
        f'Exam result for {user.username}: {"PASSED" if exam_attempt.passed else "FAILED"} '
        f'with score {exam_attempt.score or 0:.1f}%. '
        f'Completed trainings: {completed_trainings}/{total_trainings}. '
        f'Average watch completion: {avg_watch:.1f}%.'
    )
    summary = {
        'score': float(exam_attempt.score or 0),
        'passed': bool(exam_attempt.passed),
        'total_trainings_taken': total_trainings,
        'completed_trainings': completed_trainings,
        'avg_watch_percentage': round(avg_watch, 1),
    }

    obj, _ = ExamResultSummary.objects.update_or_create(
        exam_attempt=exam_attempt,
        defaults={
            'user': user,
            'course': course,
            'score': exam_attempt.score or 0,
            'passed': exam_attempt.passed,
            'total_trainings_taken': total_trainings,
            'completed_trainings': completed_trainings,
            'summary_text': summary_text,
            'data': summary,
        },
    )
    return obj


def queue_training_assignment_and_reminders(user, course):
    now = timezone.now()
    # immediate assignment reminder
    TrainingReminder.objects.get_or_create(
        user=user,
        course=course,
        reminder_type='assignment',
        due_at=now,
        defaults={'status': 'pending', 'is_active': True},
    )
    # 3-day incomplete reminder
    TrainingReminder.objects.get_or_create(
        user=user,
        course=course,
        reminder_type='incomplete',
        due_at=now + timedelta(days=3),
        defaults={'status': 'pending', 'is_active': True},
    )
    # periodic refresh reminder
    refresh_days = max(course.refresh_interval_days or 90, 1)
    TrainingReminder.objects.get_or_create(
        user=user,
        course=course,
        reminder_type='refresh',
        due_at=now + timedelta(days=refresh_days),
        defaults={'status': 'pending', 'is_active': True},
    )


def _reminder_message(reminder):
    course = reminder.course
    if reminder.reminder_type == 'assignment':
        subject = f'New SOP training assigned: {course.name}'
        html = f'<p>You have been assigned SOP training: <strong>{course.name}</strong>.</p><p>Please start your training as soon as possible.</p>'
    elif reminder.reminder_type == 'incomplete':
        subject = f'Reminder: complete SOP training for {course.name}'
        html = f'<p>This is a reminder to complete your SOP training for <strong>{course.name}</strong>.</p>'
    elif reminder.reminder_type == 'exam_due':
        subject = f'Final exam due for {course.name}'
        html = f'<p>Your final SOP exam is due for <strong>{course.name}</strong>.</p>'
    else:
        subject = f'Periodic SOP refresh required: {course.name}'
        html = f'<p>It is time to refresh your SOP training for <strong>{course.name}</strong>.</p>'
    return subject, html


def dispatch_due_reminders(limit=100):
    now = timezone.now()
    reminders = TrainingReminder.objects.select_related('user', 'course').filter(
        is_active=True,
        status__in=['pending', 'failed'],
        due_at__lte=now,
    ).order_by('due_at')[:limit]

    sent = 0
    failed = 0
    for reminder in reminders:
        user = reminder.user
        if not user.email:
            reminder.status = 'failed'
            reminder.last_error = 'User has no email'
            reminder.save(update_fields=['status', 'last_error'])
            failed += 1
            continue
        subject, html = _reminder_message(reminder)
        ok, _ = send_resend_email(
            subject=subject,
            html=html,
            to_email=user.email,
            notification_type=f'reminder_{reminder.reminder_type}',
            recipient_user=user,
            related_course=reminder.course,
        )
        reminder.sent_count += 1
        reminder.sent_at = timezone.now()
        reminder.status = 'sent' if ok else 'failed'
        reminder.last_error = '' if ok else 'resend delivery failed'
        reminder.save(update_fields=['sent_count', 'sent_at', 'status', 'last_error'])
        if ok:
            sent += 1
        else:
            failed += 1
    return {'sent': sent, 'failed': failed, 'processed': sent + failed}


def get_user_training_summary(user):
    enrollments = CourseEnrollment.objects.filter(user=user).select_related('course')
    rows = []
    for enr in enrollments:
        course = enr.course
        total = course.lessons.count()
        completed = UserProgress.objects.filter(user=user, lesson__course=course, completed=True).count()
        latest_attempt = ExamAttempt.objects.filter(user=user, exam__course=course).order_by('-started_at').first()
        rows.append({
            'course_name': course.name,
            'completed_trainings': completed,
            'total_trainings': total,
            'exam_score': latest_attempt.score if latest_attempt else None,
            'exam_passed': latest_attempt.passed if latest_attempt else None,
        })
    return rows
