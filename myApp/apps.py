from django.apps import AppConfig


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myApp'

    def ready(self):
        # Register model signals (exam summary + notification hooks)
        import myApp.signals  # noqa: F401
