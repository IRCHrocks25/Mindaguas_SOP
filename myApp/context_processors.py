def ai_generation_context(request):
    """Add AI widget state and role-aware dashboard context."""
    user = request.user
    is_authenticated = bool(getattr(user, 'is_authenticated', False))

    # Super admin can toggle "view as HR" mode for UI-only dashboard perspective.
    if is_authenticated and getattr(user, 'is_superuser', False):
        view_as = request.GET.get('view_as', '').lower()
        if view_as == 'hr':
            request.session['view_as_hr'] = True
            request.session.modified = True
        elif view_as == 'admin':
            request.session['view_as_hr'] = False
            request.session.modified = True

    is_hr_user = False
    if is_authenticated:
        profile = getattr(user, 'profile', None)
        is_hr_user = bool(profile and profile.role == 'hr')

    acting_as_hr = bool(request.session.get('view_as_hr', False)) if is_authenticated and getattr(user, 'is_superuser', False) else False
    show_hr_sidebar = is_hr_user or acting_as_hr

    role_context = {
        'is_hr_user': is_hr_user,
        'is_superadmin': bool(is_authenticated and getattr(user, 'is_superuser', False)),
        'acting_as_hr': acting_as_hr,
        'show_hr_sidebar': show_hr_sidebar,
    }

    if request.path.startswith('/dashboard/'):
        courses = request.session.get('ai_generating_courses', [])
        if not isinstance(courses, list):
            courses = []
        # Backwards compatibility: if old single-id format exists, convert
        old_id = request.session.get('ai_generating_course_id')
        if old_id and not courses:
            old_name = request.session.get('ai_generating_course_name', '')
            courses = [{'id': old_id, 'name': old_name}]
        return {'ai_generating_courses': courses, **role_context}
    return {'ai_generating_courses': [], **role_context}
