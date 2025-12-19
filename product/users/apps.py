from django.apps import AppConfig


class UsersConfig(AppConfig):
    """Класс конфигурации для приложения пользователей."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    verbose_name = 'Пользователи'
