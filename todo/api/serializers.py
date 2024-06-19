from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework import serializers

from todo_app.models import Task, Category


User = get_user_model()


class TaskSerializer(serializers.ModelSerializer):
    creator = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault(),
    )
    deadline = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    create_date = serializers.DateTimeField(
        read_only=True,
        default=serializers.CreateOnlyDefault(timezone.now),
        format='%Y-%m-%d %H:%M'
    )
    days_before_deadline = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = '__all__'

    def validate_deadline(self, value):
        if value < timezone.now():
            raise serializers.ValidationError(
                'Set the correct deadline date'
            )
        return value

    def get_days_before_deadline(self, obj):
        return (obj.deadline - timezone.now()).days


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
