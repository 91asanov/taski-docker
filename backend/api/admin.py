"""Модуль admin."""
from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """
    Административный класс для модели Task.

    Позволяет настроить отображение задач в административной панели Django.

    Атрибуты:
        list_display (tuple): Показывает указанные поля в списке объектов.
            - 'title': Название задачи.
            - 'description': Описание задачи.
            - 'completed': Статус выполнения задачи.
    """

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
