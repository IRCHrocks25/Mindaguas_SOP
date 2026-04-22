# SOP Master Function Documentation

This document inventories the current Python functions and methods in the SOP Master project.

## Scope

- Includes app logic in `myApp`, project entrypoint functions, utility functions, admin helper methods, and management command methods.
- Includes migration helper functions that contain Python logic.
- Function signatures are listed as currently implemented.

## `manage.py`

- `main()`

## `myApp/context_processors.py`

- `ai_generation_context(request)`

## `myApp/utils/transcription.py`

- `transcribe_video(video_file_path)`
- `extract_audio_from_video(video_path, audio_path)`

## `myApp/utils/notifications.py`

- `send_resend_email(subject, html, to_email, notification_type, recipient_user=None, related_course=None, related_exam_attempt=None)`
- `upsert_exam_result_summary(exam_attempt)`
- `queue_training_assignment_and_reminders(user, course)`
- `_reminder_message(reminder)`
- `dispatch_due_reminders(limit=100)`
- `get_user_training_summary(user)`

## `myApp/utils/access.py`

- `has_course_access(user, course)`
- `batch_has_course_access(user, course_ids)`
- `grant_course_access(user, course, access_type, granted_by=None, bundle_purchase=None, cohort=None, purchase_id=None, expires_at=None, notes="")`
- `revoke_course_access(user, course, revoked_by, reason="", notes="")`
- `get_user_accessible_courses(user)`
- `get_courses_by_visibility(user)`
- `check_course_prerequisites(user, course)`
- `grant_bundle_access(user, bundle_purchase)`
- `grant_cohort_access(user, cohort)`

## `myApp/views.py`

- `home(request)`
- `login_view(request)`
- `logout_view(request)`
- `courses(request)`
- `_courses_guest(request)`
- `_courses_authenticated(request)`
- `enroll_course(request, course_slug)`
- `course_detail(request, course_slug)`
- `lesson_detail(request, course_slug, lesson_slug)`
- `lesson_quiz_view(request, course_slug, lesson_slug)`
- `creator_dashboard(request)`
- `course_lessons(request, course_slug)`
- `add_lesson(request, course_slug)`
- `process_transcription()` *(nested inside `add_lesson`)*
- `_save_lesson_media_and_content(lesson, request)`
- `generate_lesson_ai(request, course_slug, lesson_id)`
- `verify_vimeo_url(request)`
- `upload_video_transcribe(request)`
- `check_transcription_status(request, lesson_id)`
- `extract_vimeo_id(url)`
- `fetch_vimeo_metadata(vimeo_id)`
- `generate_ai_lesson_content(lesson)`
- `generate_slug(text)`
- `format_duration(seconds)`
- `update_video_progress(request, lesson_id)`
- `complete_lesson(request, lesson_id)`
- `toggle_favorite_course(request, course_id)`
- `chatbot_webhook(request)`
- `student_dashboard(request)`
- `student_course_progress(request, course_slug)`
- `student_certifications(request)`
- `train_lesson_chatbot(request, lesson_id)`
- `lesson_chatbot(request, lesson_id)`

## `myApp/dashboard_views.py`

- `dashboard_home(request)`
- `dashboard_students(request)`
- `get_student_activity_feed(limit=20)`
- `dashboard_courses(request)`
- `dashboard_course_detail(request, course_slug)`
- `dashboard_delete_course(request, course_slug)`
- `dashboard_lesson_quiz(request, lesson_id)`
- `dashboard_delete_quiz(request, lesson_id)`
- `dashboard_quizzes(request)`
- `dashboard_course_lessons(request, course_slug)`
- `create_editorjs_block(block_type, data, block_id=None)`
- `create_editorjs_content(content_sections)`
- `generate_ai_lesson_metadata(client, lesson_title, lesson_description, course_name, course_type)`
- `generate_ai_lesson_content(client, lesson_title, lesson_description, course_name, course_type)`
- `generate_ai_course_structure(course_name, description, course_type='sprint', coach_name='Sprint Coach')`
- `_extract_lesson_text_for_chatbot(lesson)`
- `_send_lesson_to_chatbot_webhook(lesson)`
- `_get_ai_gen_cache_key(course_id)`
- `_update_ai_gen_progress(course_id, course_name, status, progress=0, total=0, current='', error=None)`
- `_generate_course_ai_content(course_id, course_name, description, course_type, coach_name)`
- `_remove_course_from_session(request, course_id)`
- `api_ai_generation_status(request, course_id)`
- `dashboard_add_course(request)`
- `dashboard_lessons(request)`
- `dashboard_delete_lesson(request, lesson_id)`
- `dashboard_upload_quiz(request)`
- `parse_csv_quiz(uploaded_file, quiz)`
- `generate_ai_quiz(lesson, quiz, num_questions=5)`
- `generate_ai_exam(course, exam, num_questions=20)`
- `parse_pdf_quiz(uploaded_file, quiz)`
- `dashboard_add_lesson(request)`
- `dashboard_edit_lesson(request, lesson_id)`
- `dashboard_student_progress(request)`
- `dashboard_student_detail(request, user_id, course_slug=None)`
- `dashboard_course_progress(request, course_slug)`
- `grant_course_access_view(request, user_id)`
- `revoke_course_access_view(request, user_id)`
- `grant_bundle_access_view(request, user_id)`
- `add_to_cohort_view(request, user_id)`
- `bulk_access_management(request)`
- `bulk_grant_access_view(request)`
- `dashboard_analytics(request)`
- `dashboard_hr_training_status(request)`
- `dashboard_hr_exam_results(request)`
- `dashboard_performance_correlation(request)`
- `dashboard_dispatch_reminders(request)`
- `dashboard_send_hr_digests(request)`
- `generate_slug(text)`
- `dashboard_bundles(request)`
- `dashboard_add_bundle(request)`
- `dashboard_edit_bundle(request, bundle_id)`
- `dashboard_delete_bundle(request, bundle_id)`

## `myApp/models.py`

### `Course`
- `Course.__str__(self)`
- `Course.get_lesson_count(self)`
- `Course.get_user_progress(self, user)`

### `CourseResource`
- `CourseResource.__str__(self)`
- `CourseResource.get_download_url(self)`

### `Module`
- `Module.__str__(self)`

### `Lesson`
- `Lesson.__str__(self)`
- `Lesson.get_vimeo_embed_url(self)`
- `Lesson.get_video_embed_url(self)`
- `Lesson.get_formatted_duration(self)`
- `Lesson.get_outcomes_list(self)`
- `Lesson.get_coach_actions_list(self)`

### `LessonQuiz`
- `LessonQuiz.__str__(self)`

### `LessonQuizQuestion`
- `LessonQuizQuestion.__str__(self)`

### `LessonQuizAttempt`
- `LessonQuizAttempt.__str__(self)`

### `UserProgress`
- `UserProgress.__str__(self)`
- `UserProgress.update_status(self)`

### `CourseEnrollment`
- `CourseEnrollment.__str__(self)`
- `CourseEnrollment.days_until_exam(self)`
- `CourseEnrollment.is_exam_available(self)`
- `CourseEnrollment.get_certification_status(self)`

### `FavoriteCourse`
- `FavoriteCourse.__str__(self)`

### `Exam`
- `Exam.__str__(self)`

### `ExamQuestion`
- `ExamQuestion.__str__(self)`

### `ExamAttempt`
- `ExamAttempt.__str__(self)`
- `ExamAttempt.attempt_number(self)`

### `Certification`
- `Certification.__str__(self)`

### `Cohort`
- `Cohort.__str__(self)`
- `Cohort.get_member_count(self)`

### `Bundle`
- `Bundle.__str__(self)`

### `BundlePurchase`
- `BundlePurchase.__str__(self)`

### `CourseAccess`
- `CourseAccess.__str__(self)`
- `CourseAccess.is_active(self)`
- `CourseAccess.get_source_display(self)`

### `CohortMember`
- `CohortMember.__str__(self)`

### `LearningPath`
- `LearningPath.__str__(self)`

### `LearningPathCourse`
- `LearningPathCourse.__str__(self)`

## `myApp/admin.py` (Custom admin helper methods)

- `ExamAttemptAdmin.attempt_number(self, obj)`
- `BundleAdmin.get_course_count(self, obj)`
- `CourseAccessAdmin.get_source(self, obj)`
- `LearningPathAdmin.get_course_count(self, obj)`

## Management Commands (`myApp/management/commands`)

### `add_google_drive.py`
- `Command.add_arguments(self, parser)`
- `Command.handle(self, *args, **options)`

### `check_videos.py`
- `Command.handle(self, *args, **options)`

### `clear_vimeo_use_drive.py`
- `Command.handle(self, *args, **options)`

### `fix_video_urls.py`
- `Command.handle(self, *args, **options)`

### `fix_vimeo_ids.py`
- `Command.handle(self, *args, **options)`

### `seed_additional_courses.py`
- `Command.handle(self, *args, **options)`

### `seed_lesson1_quiz.py`
- `Command.handle(self, *args, **options)`

### `send_training_reminders.py`
- `Command.handle(self, *args, **options)`

### `seed_data.py`
- `Command.add_arguments(self, parser)`
- `Command.generate_slug(self, title)`
- `Command.create_block(self, block_type, data, block_id=None)`
- `Command.create_content_blocks(self, content_sections)`
- `Command.handle(self, *args, **options)`
- `Command.create_financial_literacy_course(self)`
- `Command.create_time_management_course(self)`

## Migration Logic Functions

### `myApp/migrations/0012_alter_lesson_slug_and_add_content.py`
- `alter_slug_field(apps, schema_editor)`
- `reverse_alter_slug_field(apps, schema_editor)`

## Signals

### `myApp/signals.py`
- `handle_exam_attempt_summary_and_emails(sender, instance, created, **kwargs)`

## Notes

- This is an inventory document (function map).  
- If you want, the next step can be an expanded version with:
  - function purpose,
  - expected inputs/outputs,
  - side effects (DB/API/file I/O),
  - and endpoint URL mapping for each view function.

## SOP v2 Environment Variables

- `RESEND_API_KEY`: API key used for transactional email delivery.
- `RESEND_FROM_EMAIL`: sender identity used by Resend (e.g. verified domain mailbox).
- `HR_REPORT_EMAILS`: comma-separated HR recipient emails for status/result digests.
- `CACHE_BACKEND` / `CACHE_LOCATION`: cache backend configuration for progress + status caching.
