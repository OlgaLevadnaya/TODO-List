from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),

]

schema_view = get_schema_view(
    openapi.Info(
        title="TO-DO-LIST API",
        default_version='v1',
        description="Документация для приложения todo_app проекта TODO",
        # terms_of_service="URL страницы с пользовательским соглашением",
        # contact=openapi.Contact(email=""),
        # license=openapi.License(name=""),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    url(r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'),
]
