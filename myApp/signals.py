from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from myApp.models import ExamAttempt
from myApp.utils.notifications import send_resend_email, upsert_exam_result_summary


@receiver(post_save, sender=ExamAttempt)
def handle_exam_attempt_summary_and_emails(sender, instance, created, **kwargs):
    if not instance.completed_at and not created:
        return

    summary = upsert_exam_result_summary(instance)
    user = instance.user
    course = instance.exam.course

    if user.email:
        send_resend_email(
            subject=f'Exam Result: {course.name}',
            html=(
                f'<p>Your final exam result for <strong>{course.name}</strong> is now available.</p>'
                f'<p>Score: <strong>{summary.score:.1f}%</strong> | '
                f'Status: <strong>{"Passed" if summary.passed else "Not passed"}</strong></p>'
                f'<p>Completed trainings: {summary.completed_trainings}/{summary.total_trainings_taken}</p>'
            ),
            to_email=user.email,
            notification_type='employee_exam_result',
            recipient_user=user,
            related_course=course,
            related_exam_attempt=instance,
        )

    for hr_email in getattr(settings, 'HR_REPORT_EMAILS', []):
        send_resend_email(
            subject=f'Employee Exam Result: {user.username} - {course.name}',
            html=(
                f'<p><strong>{user.username}</strong> ({user.email}) has completed the final exam.</p>'
                f'<p>Course: {course.name}</p>'
                f'<p>Score: {summary.score:.1f}% | Passed: {"Yes" if summary.passed else "No"}</p>'
                f'<p>Completed trainings: {summary.completed_trainings}/{summary.total_trainings_taken}</p>'
            ),
            to_email=hr_email,
            notification_type='hr_exam_result',
            related_course=course,
            related_exam_attempt=instance,
        )
