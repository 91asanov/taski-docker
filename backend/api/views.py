"""Представления views."""
from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


class TaskView(viewsets.ModelViewSet):
    """
    Представление для работы с задачами (Task).

    Позволяет выполнять операции CRUD (создание, чтение, обновление, удаление)
    с задачами через REST API.
    """

    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def destroy(self, *args, **kwargs):
        """
        Переопределение метода удаления задачи.

        Возвращает сериализованные данные удаляемой задачи после её удаления.
        """
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)
