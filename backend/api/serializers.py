"""Сериализаторы API."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Task.

    Используется для преобразования данных модели Task в формат JSON
    и обратно, для API запросов и ответов.
    """

    class Meta:
        """
        Поля, включённые в сериализацию.

        - id: уникальный идентификатор задачи
        - title: название задачи
        - description: описание задачи
        - completed: статус выполнения задачи (True/False)
        """

        model = Task
        fields = ('id', 'title', 'description', 'completed')
