from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import viewsets

from todo_app.models import Category, Task
from .serializers import CategorySerializer, TaskSerializer
from rest_framework.response import Response


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(
            creator=self.request.user,
            create_date=timezone.now()
        )

    def get_queryset(self):
        return Task.objects.filter(creator=self.request.user)


class CategoryViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        pk = self.kwargs['pk']
        tasks = Task.objects.filter(category__id=pk, creator=self.request.user)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
