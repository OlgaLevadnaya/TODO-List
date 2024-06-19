from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework import serializers


from todo_app.models import Task, Category


User = get_user_model()


class TaskSerializer(serializers.ModelSerializer):
    creator = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    deadline = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    create_date = serializers.DateTimeField(
        read_only=True,
        default=timezone.now(),
        format='%Y-%m-%d %H:%M'
    )

    class Meta:
        model = Task
        fields = '__all__'

    def validate_deadline(self, value):
        if value < timezone.now():
            raise serializers.ValidationError(
                'Set the correct deadline date'
            )
        return value


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
