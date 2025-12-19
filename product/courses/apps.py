from django.apps import AppConfig


class CoursesConfig(AppConfig):
    """Конфигурация приложения для работы с курсами."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'courses'
    verbose_name = 'Курсы'

    def ready(self):
        import courses.signals
