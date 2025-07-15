"""Модуль apps."""
from django.apps import AppConfig


class ApiConfig(AppConfig):
    """
    Конфигурация приложения API.

    Атрибуты:
        default_auto_field (str):
            Тип автоматического поля для модели по умолчанию.
        name (str): Имя приложения в проекте Django.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
