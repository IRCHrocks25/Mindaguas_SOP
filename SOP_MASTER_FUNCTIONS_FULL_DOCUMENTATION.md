# SOP Master Full Function Documentation

Generated: 2026-04-22 08:39:42 UTC

This document enumerates all discovered Python functions and methods in the repository, including signatures, decorators, and short descriptions (from docstrings where available).

## Summary

- Files with functions: **21**
- Total functions/methods: **182**

## Files

- `manage.py` (1)
- `myApp/admin.py` (4)
- `myApp/apps.py` (1)
- `myApp/context_processors.py` (1)
- `myApp/dashboard_views.py` (59)
- `myApp/management/commands/add_google_drive.py` (2)
- `myApp/management/commands/check_videos.py` (1)
- `myApp/management/commands/clear_vimeo_use_drive.py` (1)
- `myApp/management/commands/fix_video_urls.py` (1)
- `myApp/management/commands/fix_vimeo_ids.py` (1)
- `myApp/management/commands/seed_additional_courses.py` (1)
- `myApp/management/commands/seed_data.py` (7)
- `myApp/management/commands/seed_lesson1_quiz.py` (1)
- `myApp/management/commands/send_training_reminders.py` (1)
- `myApp/migrations/0012_alter_lesson_slug_and_add_content.py` (2)
- `myApp/models.py` (44)
- `myApp/signals.py` (1)
- `myApp/utils/access.py` (9)
- `myApp/utils/notifications.py` (6)
- `myApp/utils/transcription.py` (2)
- `myApp/views.py` (36)

## `manage.py`

### `main`

- Type: `function`
- Signature: `main()`
- Description: Run administrative tasks.
- Defined in: `manage.py`

## `myApp/admin.py`

### `ExamAttemptAdmin.attempt_number`

- Type: `method`
- Signature: `attempt_number(self, obj)`
- Description: No docstring provided.
- Defined in: `myApp/admin.py`

### `BundleAdmin.get_course_count`

- Type: `method`
- Signature: `get_course_count(self, obj)`
- Description: No docstring provided.
- Defined in: `myApp/admin.py`

### `CourseAccessAdmin.get_source`

- Type: `method`
- Signature: `get_source(self, obj)`
- Description: No docstring provided.
- Defined in: `myApp/admin.py`

### `LearningPathAdmin.get_course_count`

- Type: `method`
- Signature: `get_course_count(self, obj)`
- Description: No docstring provided.
- Defined in: `myApp/admin.py`

## `myApp/apps.py`

### `MyappConfig.ready`

- Type: `method`
- Signature: `ready(self)`
- Description: No docstring provided.
- Defined in: `myApp/apps.py`

## `myApp/context_processors.py`

### `ai_generation_context`

- Type: `function`
- Signature: `ai_generation_context(request)`
- Description: Add AI widget state and role-aware dashboard context.
- Defined in: `myApp/context_processors.py`

## `myApp/dashboard_views.py`

### `staff_or_hr_required`

- Type: `function`
- Signature: `staff_or_hr_required(view_func)`
- Description: Allow access to staff users and users with HR role.
- Defined in: `myApp/dashboard_views.py`

### `_wrapped`

- Type: `function`
- Signature: `_wrapped(request, *args, **kwargs)`
- Description: No docstring provided.
- Decorators: `login_required`
- Defined in: `myApp/dashboard_views.py`

### `dashboard_home`

- Type: `function`
- Signature: `dashboard_home(request)`
- Description: Main dashboard overview with analytics
- Decorators: `staff_member_required`
- Defined in: `myApp/dashboard_views.py`

### `dashboard_students`

- Type: `function`
- Signature: `dashboard_students(request)`
- Description: Smart student list with activity updates and filtering
- Decorators: `staff_member_required`
- Defined in: `myApp/dashboard_views.py`

### `get_student_activity_feed`

- Type: `function`
- Signature: `get_student_activity_feed(limit=20)`
- Description: Get a comprehensive activity feed of all student activities
- Defined in: `myApp/dashboard_views.py`

### `dashboard_courses`

- Type: `function`
- Signature: `dashboard_courses(request)`
- Description: List all courses
- Decorators: `staff_member_required`
- Defined in: `myApp/dashboard_views.py`

### `dashboard_course_detail`

- Type: `function`
- Signature: `dashboard_course_detail(request, course_slug)`
- Description: Edit course details and manage resources
- Decorators: `staff_member_required`
- Defined in: `myApp/dashboard_views.py`

### `dashboard_delete_course`

- Type: `function`
- Signature: `dashboard_delete_course(request, course_slug)`
- Description: Delete a course
- Decorators: `staff_member_required, require_http_methods(['POST'])`
- Defined in: `myApp/dashboard_views.py`

### `dashboard_lesson_quiz`

- Type: `function`
- Signature: `dashboard_lesson_quiz(request, lesson_id)`
- Description: Create and manage a simple quiz for a lesson.
- Decorators: `staff_member_required`
- Defined in: `myApp/dashboard_views.py`

### `dashboard_delete_quiz`

- Type: `function`
- Signature: `dashboard_delete_quiz(request, lesson_id)`
- Description: Delete a quiz for a lesson
- Decorators: `staff_member_required, require_http_methods(['POST'])`
- Defined in: `myApp/dashboard_views.py`

### `dashboard_quizzes`

- Type: `function`
- Signature: `dashboard_quizzes(request)`
- Description: List all quizzes across all lessons
- Decorators: `staff_member_required`
- Defined in: `myApp/dashboard_views.py`

### `dashboard_course_lessons`

- Type: `function`
- Signature: `dashboard_course_lessons(request, course_slug)`
- Description: View all lessons for a course
- Decorators: `staff_member_required`
- Defined in: `myApp/dashboard_views.py`

### `create_editorjs_block`

- Type: `function`
- Signature: `create_editorjs_block(block_type, data, block_id=None)`
- Description: Create an Editor.js block
- Defined in: `myApp/dashboard_views.py`

### `create_editorjs_content`

- Type: `function`
- Signature: `create_editorjs_content(content_sections)`
- Description: Create Editor.js content blocks from content sections
- Defined in: `myApp/dashboard_views.py`

### `generate_ai_lesson_metadata`

- Type: `function`
- Signature: `generate_ai_lesson_metadata(client, lesson_title, lesson_description, course_name, course_type)`
- Description: Generate all AI lesson metadata fields (title, summary, description, outcomes, coach actions)
- Defined in: `myApp/dashboard_views.py`

### `generate_ai_lesson_content`

- Type: `function`
- Signature: `generate_ai_lesson_content(client, lesson_title, lesson_description, course_name, course_type)`
- Description: Generate detailed lesson content using AI (Editor.js blocks)
- Defined in: `myApp/dashboard_views.py`

### `generate_ai_course_structure`

- Type: `function`
- Signature: `generate_ai_course_structure(course_name, description, course_type='sprint', coach_name='Sprint Coach', is_sop_program=False, sop_guidelines='')`
- Description: Generate complete course structure (modules and lessons) using AI
- Defined in: `myApp/dashboard_views.py`

### `_extract_lesson_text_for_chatbot`

- Type: `function`
- Signature: `_extract_lesson_text_for_chatbot(lesson)`
- Description: Extract text content from lesson for chatbot training (transcript replacement for AI-generated lessons)
- Defined in: `myApp/dashboard_views.py`

### `_send_lesson_to_chatbot_webhook`

- Type: `function`
- Signature: `_send_lesson_to_chatbot_webhook(lesson)`
- Description: Send lesson content to training webhook for AI chatbot. Returns True on success, False on failure.
- Defined in: `myApp/dashboard_views.py`

### `_get_ai_gen_cache_key`

- Type: `function`
- Signature: `_get_ai_gen_cache_key(course_id)`
- Description: No docstring provided.
- Defined in: `myApp/dashboard_views.py`

### `_update_ai_gen_progress`

- Type: `function`
- Signature: `_update_ai_gen_progress(course_id, course_name, status, progress=0, total=0, current='', error=None)`
- Description: Update AI generation progress in cache (15 min TTL)
- Defined in: `myApp/dashboard_views.py`

### `_generate_course_ai_content`

- Type: `function`
- Signature: `_generate_course_ai_content(course_id, course_name, description, course_type, coach_name, is_sop_program=False, sop_guidelines='')`
- Description: Background function to generate AI course content
- Defined in: `myApp/dashboard_views.py`

### `_remove_course_from_session`

- Type: `function`
- Signature: `_remove_course_from_session(request, course_id)`
- Description: Remove a single course from the ai_generating_courses list
- Defined in: `myApp/dashboard_views.py`

### `api_ai_generation_status`

- Type: `function`
- Signature: `api_ai_generation_status(request, course_id)`
- Description: JSON endpoint for polling AI course generation progress
- Decorators: `staff_member_required`
- Defined in: `myApp/dashboard_views.py`

### `dashboard_add_course`

- Type: `function`
- Signature: `dashboard_add_course(request)`
- Description: Add new course with optional AI generation
- Decorators: `staff_member_required`
- Defined in: `myApp/dashboard_views.py`

### `dashboard_lessons`

- Type: `function`
- Signature: `dashboard_lessons(request)`
- Description: List all lessons across all courses
- Decorators: `staff_member_required`
- Defined in: `myApp/dashboard_views.py`

### `dashboard_delete_lesson`

- Type: `function`
- Signature: `dashboard_delete_lesson(request, lesson_id)`
- Description: Delete a lesson
- Decorators: `staff_member_required, require_http_methods(['POST'])`
- Defined in: `myApp/dashboard_views.py`

### `dashboard_upload_quiz`

- Type: `function`
- Signature: `dashboard_upload_quiz(request)`
- Description: Upload quiz from CSV/PDF file or generate with AI
- Decorators: `staff_member_required`
- Defined in: `myApp/dashboard_views.py`

### `parse_csv_quiz`

- Type: `function`
- Signature: `parse_csv_quiz(uploaded_file, quiz)`
- Description: Parse CSV file and create quiz questions
- Defined in: `myApp/dashboard_views.py`

### `generate_ai_quiz`

- Type: `function`
- Signature: `generate_ai_quiz(lesson, quiz, num_questions=5)`
- Description: Generate quiz questions using AI based on lesson content
- Defined in: `myApp/dashboard_views.py`

### `generate_ai_exam`

- Type: `function`
- Signature: `generate_ai_exam(course, exam, num_questions=20)`
- Description: Generate final exam questions using AI based on full course content.
- Defined in: `myApp/dashboard_views.py`

### `parse_pdf_quiz`

- Type: `function`
- Signature: `parse_pdf_quiz(uploaded_file, quiz)`
- Description: Parse PDF file and create quiz questions
- Defined in: `myApp/dashboard_views.py`

### `dashboard_add_lesson`

- Type: `function`
- Signature: `dashboard_add_lesson(request)`
- Description: Add new lesson - redirects to creator flow
- Decorators: `staff_member_required`
- Defined in: `myApp/dashboard_views.py`

### `dashboard_edit_lesson`

- Type: `function`
- Signature: `dashboard_edit_lesson(request, lesson_id)`
- Description: Edit lesson - redirects to AI generation page
- Decorators: `staff_member_required`
- Defined in: `myApp/dashboard_views.py`

### `dashboard_student_progress`

- Type: `function`
- Signature: `dashboard_student_progress(request)`
- Description: Student progress overview - all students
- Decorators: `staff_member_required`
- Defined in: `myApp/dashboard_views.py`

### `dashboard_student_detail`

- Type: `function`
- Signature: `dashboard_student_detail(request, user_id, course_slug=None)`
- Description: Detailed student progress view
- Decorators: `staff_member_required`
- Defined in: `myApp/dashboard_views.py`

### `dashboard_course_progress`

- Type: `function`
- Signature: `dashboard_course_progress(request, course_slug)`
- Description: View all student progress for a specific course
- Decorators: `staff_member_required`
- Defined in: `myApp/dashboard_views.py`

### `grant_course_access_view`

- Type: `function`
- Signature: `grant_course_access_view(request, user_id)`
- Description: Grant course access to a student
- Decorators: `staff_member_required, require_http_methods(['POST'])`
- Defined in: `myApp/dashboard_views.py`

### `revoke_course_access_view`

- Type: `function`
- Signature: `revoke_course_access_view(request, user_id)`
- Description: Revoke course access from a student
- Decorators: `staff_member_required, require_http_methods(['POST'])`
- Defined in: `myApp/dashboard_views.py`

### `grant_bundle_access_view`

- Type: `function`
- Signature: `grant_bundle_access_view(request, user_id)`
- Description: Grant bundle access to a student
- Decorators: `staff_member_required, require_http_methods(['POST'])`
- Defined in: `myApp/dashboard_views.py`

### `add_to_cohort_view`

- Type: `function`
- Signature: `add_to_cohort_view(request, user_id)`
- Description: Add student to a cohort
- Decorators: `staff_member_required, require_http_methods(['POST'])`
- Defined in: `myApp/dashboard_views.py`

### `bulk_access_management`

- Type: `function`
- Signature: `bulk_access_management(request)`
- Description: Bulk access management page
- Decorators: `staff_member_required`
- Defined in: `myApp/dashboard_views.py`

### `bulk_grant_access_view`

- Type: `function`
- Signature: `bulk_grant_access_view(request)`
- Description: Bulk grant course access to multiple students
- Decorators: `staff_member_required, require_http_methods(['POST'])`
- Defined in: `myApp/dashboard_views.py`

### `dashboard_analytics`

- Type: `function`
- Signature: `dashboard_analytics(request)`
- Description: Comprehensive analytics dashboard
- Decorators: `staff_member_required`
- Defined in: `myApp/dashboard_views.py`

### `dashboard_hr_training_status`

- Type: `function`
- Signature: `dashboard_hr_training_status(request)`
- Description: HR view: status of trainings for each employee.
- Decorators: `staff_or_hr_required`
- Defined in: `myApp/dashboard_views.py`

### `dashboard_hr_exam_results`

- Type: `function`
- Signature: `dashboard_hr_exam_results(request)`
- Description: HR view: exam results plus training summary.
- Decorators: `staff_or_hr_required`
- Defined in: `myApp/dashboard_views.py`

### `dashboard_course_email_report`

- Type: `function`
- Signature: `dashboard_course_email_report(request)`
- Description: Report of course-assignment emails and learner progress state.
- Decorators: `staff_or_hr_required`
- Defined in: `myApp/dashboard_views.py`

### `dashboard_hr_employee_report`

- Type: `function`
- Signature: `dashboard_hr_employee_report(request, user_id)`
- Description: Detailed per-employee report across trainings, exams, emails, reminders, and performance.
- Decorators: `staff_or_hr_required`
- Defined in: `myApp/dashboard_views.py`

### `dashboard_performance_correlation`

- Type: `function`
- Signature: `dashboard_performance_correlation(request)`
- Description: Manual performance entry + correlation with training and exam outcomes.
- Decorators: `staff_or_hr_required, require_http_methods(['GET', 'POST'])`
- Defined in: `myApp/dashboard_views.py`

### `dashboard_dispatch_reminders`

- Type: `function`
- Signature: `dashboard_dispatch_reminders(request)`
- Description: Trigger reminder dispatch manually from dashboard.
- Decorators: `staff_or_hr_required, require_http_methods(['POST'])`
- Defined in: `myApp/dashboard_views.py`

### `dashboard_send_hr_digests`

- Type: `function`
- Signature: `dashboard_send_hr_digests(request)`
- Description: Send HR digest emails with employee training and exam status.
- Decorators: `staff_or_hr_required, require_http_methods(['POST'])`
- Defined in: `myApp/dashboard_views.py`

### `dashboard_send_course_assignment_email`

- Type: `function`
- Signature: `dashboard_send_course_assignment_email(request)`
- Description: Send a specific course assignment email to a selected employee.
- Decorators: `staff_or_hr_required, require_http_methods(['POST'])`
- Defined in: `myApp/dashboard_views.py`

### `_username_from_email`

- Type: `function`
- Signature: `_username_from_email(email)`
- Description: No docstring provided.
- Defined in: `myApp/dashboard_views.py`

### `dashboard_hr_accounts`

- Type: `function`
- Signature: `dashboard_hr_accounts(request)`
- Description: Super admin creates HR accounts and sends invitation email.
- Decorators: `staff_member_required, require_http_methods(['GET', 'POST'])`
- Defined in: `myApp/dashboard_views.py`

### `generate_slug`

- Type: `function`
- Signature: `generate_slug(text)`
- Description: Generate URL-friendly slug from text
- Defined in: `myApp/dashboard_views.py`

### `dashboard_bundles`

- Type: `function`
- Signature: `dashboard_bundles(request)`
- Description: List all bundles
- Decorators: `staff_member_required`
- Defined in: `myApp/dashboard_views.py`

### `dashboard_add_bundle`

- Type: `function`
- Signature: `dashboard_add_bundle(request)`
- Description: Create a new bundle
- Decorators: `staff_member_required`
- Defined in: `myApp/dashboard_views.py`

### `dashboard_edit_bundle`

- Type: `function`
- Signature: `dashboard_edit_bundle(request, bundle_id)`
- Description: Edit an existing bundle
- Decorators: `staff_member_required`
- Defined in: `myApp/dashboard_views.py`

### `dashboard_delete_bundle`

- Type: `function`
- Signature: `dashboard_delete_bundle(request, bundle_id)`
- Description: Delete a bundle
- Decorators: `staff_member_required, require_http_methods(['POST'])`
- Defined in: `myApp/dashboard_views.py`

## `myApp/management/commands/add_google_drive.py`

### `Command.add_arguments`

- Type: `method`
- Signature: `add_arguments(self, parser)`
- Description: No docstring provided.
- Defined in: `myApp/management/commands/add_google_drive.py`

### `Command.handle`

- Type: `method`
- Signature: `handle(self, *args, **options)`
- Description: No docstring provided.
- Defined in: `myApp/management/commands/add_google_drive.py`

## `myApp/management/commands/check_videos.py`

### `Command.handle`

- Type: `method`
- Signature: `handle(self, *args, **options)`
- Description: No docstring provided.
- Defined in: `myApp/management/commands/check_videos.py`

## `myApp/management/commands/clear_vimeo_use_drive.py`

### `Command.handle`

- Type: `method`
- Signature: `handle(self, *args, **options)`
- Description: No docstring provided.
- Defined in: `myApp/management/commands/clear_vimeo_use_drive.py`

## `myApp/management/commands/fix_video_urls.py`

### `Command.handle`

- Type: `method`
- Signature: `handle(self, *args, **options)`
- Description: No docstring provided.
- Defined in: `myApp/management/commands/fix_video_urls.py`

## `myApp/management/commands/fix_vimeo_ids.py`

### `Command.handle`

- Type: `method`
- Signature: `handle(self, *args, **options)`
- Description: No docstring provided.
- Defined in: `myApp/management/commands/fix_vimeo_ids.py`

## `myApp/management/commands/seed_additional_courses.py`

### `Command.handle`

- Type: `method`
- Signature: `handle(self, *args, **options)`
- Description: No docstring provided.
- Defined in: `myApp/management/commands/seed_additional_courses.py`

## `myApp/management/commands/seed_data.py`

### `Command.add_arguments`

- Type: `method`
- Signature: `add_arguments(self, parser)`
- Description: No docstring provided.
- Defined in: `myApp/management/commands/seed_data.py`

### `Command.generate_slug`

- Type: `method`
- Signature: `generate_slug(self, title)`
- Description: Generate a URL-friendly slug from a title
- Defined in: `myApp/management/commands/seed_data.py`

### `Command.create_block`

- Type: `method`
- Signature: `create_block(self, block_type, data, block_id=None)`
- Description: Create an Editor.js block
- Defined in: `myApp/management/commands/seed_data.py`

### `Command.create_content_blocks`

- Type: `method`
- Signature: `create_content_blocks(self, content_sections)`
- Description: Create Editor.js blocks from content sections
- Defined in: `myApp/management/commands/seed_data.py`

### `Command.handle`

- Type: `method`
- Signature: `handle(self, *args, **options)`
- Description: No docstring provided.
- Defined in: `myApp/management/commands/seed_data.py`

### `Command.create_financial_literacy_course`

- Type: `method`
- Signature: `create_financial_literacy_course(self)`
- Description: Create Financial Literacy course with lessons
- Defined in: `myApp/management/commands/seed_data.py`

### `Command.create_time_management_course`

- Type: `method`
- Signature: `create_time_management_course(self)`
- Description: Create Time Management Mastery course with lessons
- Defined in: `myApp/management/commands/seed_data.py`

## `myApp/management/commands/seed_lesson1_quiz.py`

### `Command.handle`

- Type: `method`
- Signature: `handle(self, *args, **options)`
- Description: No docstring provided.
- Defined in: `myApp/management/commands/seed_lesson1_quiz.py`

## `myApp/management/commands/send_training_reminders.py`

### `Command.handle`

- Type: `method`
- Signature: `handle(self, *args, **options)`
- Description: No docstring provided.
- Defined in: `myApp/management/commands/send_training_reminders.py`

## `myApp/migrations/0012_alter_lesson_slug_and_add_content.py`

### `alter_slug_field`

- Type: `function`
- Signature: `alter_slug_field(apps, schema_editor)`
- Description: Alter the slug field to allow 200 characters
- Defined in: `myApp/migrations/0012_alter_lesson_slug_and_add_content.py`

### `reverse_alter_slug_field`

- Type: `function`
- Signature: `reverse_alter_slug_field(apps, schema_editor)`
- Description: Reverse: change slug back to 50 characters
- Defined in: `myApp/migrations/0012_alter_lesson_slug_and_add_content.py`

## `myApp/models.py`

### `Course.__str__`

- Type: `method`
- Signature: `__str__(self)`
- Description: No docstring provided.
- Defined in: `myApp/models.py`

### `Course.get_lesson_count`

- Type: `method`
- Signature: `get_lesson_count(self)`
- Description: No docstring provided.
- Defined in: `myApp/models.py`

### `Course.get_user_progress`

- Type: `method`
- Signature: `get_user_progress(self, user)`
- Description: No docstring provided.
- Defined in: `myApp/models.py`

### `CourseResource.__str__`

- Type: `method`
- Signature: `__str__(self)`
- Description: No docstring provided.
- Defined in: `myApp/models.py`

### `CourseResource.get_download_url`

- Type: `method`
- Signature: `get_download_url(self)`
- Description: Return the URL to download this resource (file or external link)
- Defined in: `myApp/models.py`

### `Module.__str__`

- Type: `method`
- Signature: `__str__(self)`
- Description: No docstring provided.
- Defined in: `myApp/models.py`

### `Lesson.__str__`

- Type: `method`
- Signature: `__str__(self)`
- Description: No docstring provided.
- Defined in: `myApp/models.py`

### `Lesson.get_vimeo_embed_url`

- Type: `method`
- Signature: `get_vimeo_embed_url(self)`
- Description: Convert Vimeo URL to embed format
- Defined in: `myApp/models.py`

### `Lesson.get_video_embed_url`

- Type: `method`
- Signature: `get_video_embed_url(self)`
- Description: Convert video_url to embed format. YouTube watch/short URLs must use embed format for iframes.
- Defined in: `myApp/models.py`

### `Lesson.get_formatted_duration`

- Type: `method`
- Signature: `get_formatted_duration(self)`
- Description: Format duration in MM:SS format
- Defined in: `myApp/models.py`

### `Lesson.get_outcomes_list`

- Type: `method`
- Signature: `get_outcomes_list(self)`
- Description: Return outcomes as a list
- Defined in: `myApp/models.py`

### `Lesson.get_coach_actions_list`

- Type: `method`
- Signature: `get_coach_actions_list(self)`
- Description: Return coach actions as a list
- Defined in: `myApp/models.py`

### `LessonQuiz.__str__`

- Type: `method`
- Signature: `__str__(self)`
- Description: No docstring provided.
- Defined in: `myApp/models.py`

### `LessonQuizQuestion.__str__`

- Type: `method`
- Signature: `__str__(self)`
- Description: No docstring provided.
- Defined in: `myApp/models.py`

### `LessonQuizAttempt.__str__`

- Type: `method`
- Signature: `__str__(self)`
- Description: No docstring provided.
- Defined in: `myApp/models.py`

### `UserProgress.__str__`

- Type: `method`
- Signature: `__str__(self)`
- Description: No docstring provided.
- Defined in: `myApp/models.py`

### `UserProgress.update_status`

- Type: `method`
- Signature: `update_status(self)`
- Description: Automatically update status based on progress
- Defined in: `myApp/models.py`

### `CourseEnrollment.__str__`

- Type: `method`
- Signature: `__str__(self)`
- Description: No docstring provided.
- Defined in: `myApp/models.py`

### `CourseEnrollment.days_until_exam`

- Type: `method`
- Signature: `days_until_exam(self)`
- Description: No docstring provided.
- Defined in: `myApp/models.py`

### `CourseEnrollment.is_exam_available`

- Type: `method`
- Signature: `is_exam_available(self)`
- Description: Check if exam is available based on payment type and course completion
- Defined in: `myApp/models.py`

### `CourseEnrollment.get_certification_status`

- Type: `method`
- Signature: `get_certification_status(self)`
- Description: Get current certification status
- Defined in: `myApp/models.py`

### `FavoriteCourse.__str__`

- Type: `method`
- Signature: `__str__(self)`
- Description: No docstring provided.
- Defined in: `myApp/models.py`

### `Exam.__str__`

- Type: `method`
- Signature: `__str__(self)`
- Description: No docstring provided.
- Defined in: `myApp/models.py`

### `ExamQuestion.__str__`

- Type: `method`
- Signature: `__str__(self)`
- Description: No docstring provided.
- Defined in: `myApp/models.py`

### `ExamAttempt.__str__`

- Type: `method`
- Signature: `__str__(self)`
- Description: No docstring provided.
- Defined in: `myApp/models.py`

### `ExamAttempt.attempt_number`

- Type: `method`
- Signature: `attempt_number(self)`
- Description: Get the attempt number for this user and exam
- Defined in: `myApp/models.py`

### `Certification.__str__`

- Type: `method`
- Signature: `__str__(self)`
- Description: No docstring provided.
- Defined in: `myApp/models.py`

### `Cohort.__str__`

- Type: `method`
- Signature: `__str__(self)`
- Description: No docstring provided.
- Defined in: `myApp/models.py`

### `Cohort.get_member_count`

- Type: `method`
- Signature: `get_member_count(self)`
- Description: No docstring provided.
- Defined in: `myApp/models.py`

### `Bundle.__str__`

- Type: `method`
- Signature: `__str__(self)`
- Description: No docstring provided.
- Defined in: `myApp/models.py`

### `BundlePurchase.__str__`

- Type: `method`
- Signature: `__str__(self)`
- Description: No docstring provided.
- Defined in: `myApp/models.py`

### `CourseAccess.__str__`

- Type: `method`
- Signature: `__str__(self)`
- Description: No docstring provided.
- Defined in: `myApp/models.py`

### `CourseAccess.is_active`

- Type: `method`
- Signature: `is_active(self)`
- Description: Check if access is currently active
- Defined in: `myApp/models.py`

### `CourseAccess.get_source_display`

- Type: `method`
- Signature: `get_source_display(self)`
- Description: Get human-readable source of access
- Defined in: `myApp/models.py`

### `CohortMember.__str__`

- Type: `method`
- Signature: `__str__(self)`
- Description: No docstring provided.
- Defined in: `myApp/models.py`

### `LearningPath.__str__`

- Type: `method`
- Signature: `__str__(self)`
- Description: No docstring provided.
- Defined in: `myApp/models.py`

### `LearningPathCourse.__str__`

- Type: `method`
- Signature: `__str__(self)`
- Description: No docstring provided.
- Defined in: `myApp/models.py`

### `TrainingReminder.__str__`

- Type: `method`
- Signature: `__str__(self)`
- Description: No docstring provided.
- Defined in: `myApp/models.py`

### `EmailNotificationLog.__str__`

- Type: `method`
- Signature: `__str__(self)`
- Description: No docstring provided.
- Defined in: `myApp/models.py`

### `ExamResultSummary.__str__`

- Type: `method`
- Signature: `__str__(self)`
- Description: No docstring provided.
- Defined in: `myApp/models.py`

### `EmployeePerformanceMetric.__str__`

- Type: `method`
- Signature: `__str__(self)`
- Description: No docstring provided.
- Defined in: `myApp/models.py`

### `UserProfile.__str__`

- Type: `method`
- Signature: `__str__(self)`
- Description: No docstring provided.
- Defined in: `myApp/models.py`

### `HRInvitation.__str__`

- Type: `method`
- Signature: `__str__(self)`
- Description: No docstring provided.
- Defined in: `myApp/models.py`

### `HRInvitation.is_expired`

- Type: `method`
- Signature: `is_expired(self)`
- Description: No docstring provided.
- Defined in: `myApp/models.py`

## `myApp/signals.py`

### `handle_exam_attempt_summary_and_emails`

- Type: `function`
- Signature: `handle_exam_attempt_summary_and_emails(sender, instance, created, **kwargs)`
- Description: No docstring provided.
- Decorators: `receiver(post_save, sender=ExamAttempt)`
- Defined in: `myApp/signals.py`

## `myApp/utils/access.py`

### `has_course_access`

- Type: `function`
- Signature: `has_course_access(user, course)`
- Description: Check if user has active access to a course.
- Defined in: `myApp/utils/access.py`

### `batch_has_course_access`

- Type: `function`
- Signature: `batch_has_course_access(user, course_ids)`
- Description: Batch check course access for multiple courses. Returns dict: course_id -> (has_access, access_record, reason)
- Defined in: `myApp/utils/access.py`

### `grant_course_access`

- Type: `function`
- Signature: `grant_course_access(user, course, access_type, granted_by=None, bundle_purchase=None, cohort=None, purchase_id=None, expires_at=None, notes='')`
- Description: Grant access to a course.
- Defined in: `myApp/utils/access.py`

### `revoke_course_access`

- Type: `function`
- Signature: `revoke_course_access(user, course, revoked_by, reason='', notes='')`
- Description: Revoke access to a course.
- Defined in: `myApp/utils/access.py`

### `get_user_accessible_courses`

- Type: `function`
- Signature: `get_user_accessible_courses(user)`
- Description: Get all courses the user has active access to.
- Defined in: `myApp/utils/access.py`

### `get_courses_by_visibility`

- Type: `function`
- Signature: `get_courses_by_visibility(user)`
- Description: Get courses organized by visibility rules.
- Defined in: `myApp/utils/access.py`

### `check_course_prerequisites`

- Type: `function`
- Signature: `check_course_prerequisites(user, course)`
- Description: Check if user has met prerequisites for a course.
- Defined in: `myApp/utils/access.py`

### `grant_bundle_access`

- Type: `function`
- Signature: `grant_bundle_access(user, bundle_purchase)`
- Description: Grant access to all courses in a bundle purchase.
- Defined in: `myApp/utils/access.py`

### `grant_cohort_access`

- Type: `function`
- Signature: `grant_cohort_access(user, cohort)`
- Description: Grant access to all courses associated with a cohort.
- Defined in: `myApp/utils/access.py`

## `myApp/utils/notifications.py`

### `send_resend_email`

- Type: `function`
- Signature: `send_resend_email(subject, html, to_email, notification_type, recipient_user=None, related_course=None, related_exam_attempt=None)`
- Description: No docstring provided.
- Defined in: `myApp/utils/notifications.py`

### `upsert_exam_result_summary`

- Type: `function`
- Signature: `upsert_exam_result_summary(exam_attempt)`
- Description: No docstring provided.
- Defined in: `myApp/utils/notifications.py`

### `queue_training_assignment_and_reminders`

- Type: `function`
- Signature: `queue_training_assignment_and_reminders(user, course)`
- Description: No docstring provided.
- Defined in: `myApp/utils/notifications.py`

### `_reminder_message`

- Type: `function`
- Signature: `_reminder_message(reminder)`
- Description: No docstring provided.
- Defined in: `myApp/utils/notifications.py`

### `dispatch_due_reminders`

- Type: `function`
- Signature: `dispatch_due_reminders(limit=100)`
- Description: No docstring provided.
- Defined in: `myApp/utils/notifications.py`

### `get_user_training_summary`

- Type: `function`
- Signature: `get_user_training_summary(user)`
- Description: No docstring provided.
- Defined in: `myApp/utils/notifications.py`

## `myApp/utils/transcription.py`

### `transcribe_video`

- Type: `function`
- Signature: `transcribe_video(video_file_path)`
- Description: Transcribe video file to text.
- Defined in: `myApp/utils/transcription.py`

### `extract_audio_from_video`

- Type: `function`
- Signature: `extract_audio_from_video(video_path, audio_path)`
- Description: Extract audio from video file using ffmpeg.
- Defined in: `myApp/utils/transcription.py`

## `myApp/views.py`

### `home`

- Type: `function`
- Signature: `home(request)`
- Description: Home page view - shows landing page
- Defined in: `myApp/views.py`

### `_post_login_redirect_name`

- Type: `function`
- Signature: `_post_login_redirect_name(user)`
- Description: No docstring provided.
- Defined in: `myApp/views.py`

### `login_view`

- Type: `function`
- Signature: `login_view(request)`
- Description: Premium login page
- Defined in: `myApp/views.py`

### `logout_view`

- Type: `function`
- Signature: `logout_view(request)`
- Description: Logout view
- Defined in: `myApp/views.py`

### `accept_hr_invitation`

- Type: `function`
- Signature: `accept_hr_invitation(request, token)`
- Description: Accept HR invitation and set account password.
- Defined in: `myApp/views.py`

### `hr_dashboard`

- Type: `function`
- Signature: `hr_dashboard(request)`
- Description: Dedicated dashboard for HR role.
- Decorators: `login_required`
- Defined in: `myApp/views.py`

### `courses`

- Type: `function`
- Signature: `courses(request)`
- Description: Unified learning hub: dashboard for logged-in users, catalog for guests.
- Defined in: `myApp/views.py`

### `_courses_guest`

- Type: `function`
- Signature: `_courses_guest(request)`
- Description: Catalog view for logged-out users
- Defined in: `myApp/views.py`

### `_courses_authenticated`

- Type: `function`
- Signature: `_courses_authenticated(request)`
- Description: Full dashboard for logged-in users - merges dashboard + courses
- Defined in: `myApp/views.py`

### `enroll_course`

- Type: `function`
- Signature: `enroll_course(request, course_slug)`
- Description: Enroll in a course (self-enrollment for open-enrollment courses) and redirect to course.
- Decorators: `login_required`
- Defined in: `myApp/views.py`

### `course_detail`

- Type: `function`
- Signature: `course_detail(request, course_slug)`
- Description: Course detail page - redirects to first lesson or course overview. Shows enroll option if no access.
- Decorators: `login_required`
- Defined in: `myApp/views.py`

### `lesson_detail`

- Type: `function`
- Signature: `lesson_detail(request, course_slug, lesson_slug)`
- Description: Lesson detail page with three-column layout
- Decorators: `login_required`
- Defined in: `myApp/views.py`

### `lesson_quiz_view`

- Type: `function`
- Signature: `lesson_quiz_view(request, course_slug, lesson_slug)`
- Description: Simple multiple‑choice quiz attached to a lesson (optional).
- Decorators: `login_required`
- Defined in: `myApp/views.py`

### `creator_dashboard`

- Type: `function`
- Signature: `creator_dashboard(request)`
- Description: Main creator dashboard
- Decorators: `staff_member_required`
- Defined in: `myApp/views.py`

### `course_lessons`

- Type: `function`
- Signature: `course_lessons(request, course_slug)`
- Description: View all lessons for a course
- Decorators: `staff_member_required`
- Defined in: `myApp/views.py`

### `add_lesson`

- Type: `function`
- Signature: `add_lesson(request, course_slug)`
- Description: Add new lesson - 3-step flow with video upload and transcription
- Decorators: `staff_member_required`
- Defined in: `myApp/views.py`

### `process_transcription`

- Type: `function`
- Signature: `process_transcription()`
- Description: No docstring provided.
- Defined in: `myApp/views.py`

### `_save_lesson_media_and_content`

- Type: `function`
- Signature: `_save_lesson_media_and_content(lesson, request)`
- Description: Save video URLs, workbook, resources, and content blocks from POST.
- Defined in: `myApp/views.py`

### `generate_lesson_ai`

- Type: `function`
- Signature: `generate_lesson_ai(request, course_slug, lesson_id)`
- Description: Generate AI content for lesson
- Decorators: `staff_member_required`
- Defined in: `myApp/views.py`

### `verify_vimeo_url`

- Type: `function`
- Signature: `verify_vimeo_url(request)`
- Description: AJAX endpoint to verify Vimeo URL and fetch metadata
- Decorators: `require_http_methods(['POST']), staff_member_required`
- Defined in: `myApp/views.py`

### `upload_video_transcribe`

- Type: `function`
- Signature: `upload_video_transcribe(request)`
- Description: AJAX endpoint to upload video and start transcription - video is NOT saved, only used temporarily
- Decorators: `require_http_methods(['POST']), staff_member_required`
- Defined in: `myApp/views.py`

### `check_transcription_status`

- Type: `function`
- Signature: `check_transcription_status(request, lesson_id)`
- Description: AJAX endpoint to check transcription status
- Decorators: `require_http_methods(['POST']), staff_member_required`
- Defined in: `myApp/views.py`

### `extract_vimeo_id`

- Type: `function`
- Signature: `extract_vimeo_id(url)`
- Description: Extract Vimeo video ID from URL
- Defined in: `myApp/views.py`

### `fetch_vimeo_metadata`

- Type: `function`
- Signature: `fetch_vimeo_metadata(vimeo_id)`
- Description: Fetch metadata from Vimeo API (using oEmbed endpoint)
- Defined in: `myApp/views.py`

### `generate_ai_lesson_content`

- Type: `function`
- Signature: `generate_ai_lesson_content(lesson)`
- Description: Generate AI content for lesson (placeholder - connect to OpenAI later)
- Defined in: `myApp/views.py`

### `generate_slug`

- Type: `function`
- Signature: `generate_slug(text)`
- Description: Generate URL-friendly slug from text
- Defined in: `myApp/views.py`

### `format_duration`

- Type: `function`
- Signature: `format_duration(seconds)`
- Description: Format seconds as MM:SS
- Defined in: `myApp/views.py`

### `update_video_progress`

- Type: `function`
- Signature: `update_video_progress(request, lesson_id)`
- Description: Update video watch progress for a lesson
- Decorators: `require_http_methods(['POST']), login_required`
- Defined in: `myApp/views.py`

### `complete_lesson`

- Type: `function`
- Signature: `complete_lesson(request, lesson_id)`
- Description: Mark a lesson as complete for the current user.
- Decorators: `require_http_methods(['POST']), login_required`
- Defined in: `myApp/views.py`

### `toggle_favorite_course`

- Type: `function`
- Signature: `toggle_favorite_course(request, course_id)`
- Description: Toggle favorite status for a course
- Decorators: `require_http_methods(['POST']), login_required`
- Defined in: `myApp/views.py`

### `chatbot_webhook`

- Type: `function`
- Signature: `chatbot_webhook(request)`
- Description: Forward chatbot messages to the appropriate webhook based on lesson
- Decorators: `require_http_methods(['POST']), login_required`
- Defined in: `myApp/views.py`

### `student_dashboard`

- Type: `function`
- Signature: `student_dashboard(request)`
- Description: Redirect to unified courses hub (same content as /courses/ for logged-in users).
- Defined in: `myApp/views.py`

### `student_course_progress`

- Type: `function`
- Signature: `student_course_progress(request, course_slug)`
- Description: Detailed progress view for a specific course
- Decorators: `login_required`
- Defined in: `myApp/views.py`

### `student_certifications`

- Type: `function`
- Signature: `student_certifications(request)`
- Description: View all certifications
- Decorators: `login_required`
- Defined in: `myApp/views.py`

### `train_lesson_chatbot`

- Type: `function`
- Signature: `train_lesson_chatbot(request, lesson_id)`
- Description: Send transcript to training webhook and update lesson status
- Decorators: `staff_member_required, require_http_methods(['POST'])`
- Defined in: `myApp/views.py`

### `lesson_chatbot`

- Type: `function`
- Signature: `lesson_chatbot(request, lesson_id)`
- Description: Handle chatbot interactions for a lesson
- Decorators: `login_required, require_http_methods(['POST'])`
- Defined in: `myApp/views.py`
