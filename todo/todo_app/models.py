from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Category(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Category'
    )

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.title


class Task(models.Model):
    IMPORTANCE_CHOICES = (
        ('LI', 'Low importance'),
        ('AI', 'Average importance'),
        ('HI', 'High importance'),
    )
    text = models.TextField('Task')
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Task creator',
    )
    create_date = models.DateTimeField(
        verbose_name='Date of creation',
        auto_now_add=True
    )
    deadline = models.DateTimeField(
        verbose_name='Deadline date'
    )
    done = models.BooleanField(
        verbose_name='Task completed'
    )
    importance = models.CharField(
        'Importance',
        max_length=25,
        choices=IMPORTANCE_CHOICES
    )
    category = models.ForeignKey(
        Category,
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
