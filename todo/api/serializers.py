from django.contrib.auth import get_user_model
from rest_framework import serializers

from todo_app.models import Task, Category


User = get_user_model()


class TaskSerializer(serializers.ModelSerializer):
    creator = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Task
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
