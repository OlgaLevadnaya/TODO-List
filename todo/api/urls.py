from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import CategoryViewSet, TaskViewSet


router = SimpleRouter()

router.register('tasks', TaskViewSet, basename='tasks')
router.register('categories', CategoryViewSet, basename='categories')

urlpatterns = [
    path('v1/auth/', include('djoser.urls')),
    path('v1/auth/', include('djoser.urls.jwt')),
    path('v1/', include(router.urls))
]
