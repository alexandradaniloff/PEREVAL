from django.contrib import admin
from django.urls import path, include
import django_filters
from rest_framework.response import Response
from rest_framework import viewsets, status

from rest_framework.routers import DefaultRouter
from django.urls import path, include, re_path
from rest_framework import routers
from django.contrib import admin
from project.views import *
from django.views.generic import TemplateView
from rest_framework import permissions

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Perevals API",
        default_version="v1",
        description="This API provides access to data and services for our project",
        terms_of_service="",  # Здесь может быть ссылка на условия использования (пустая строка в данном случае)
        contact=openapi.Contact(email="contact@example.com"),  # Здесь указывается контактный email
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger-ui',
         TemplateView.as_view(template_name='swagger-ui.html', extra_context={'schema_url': 'schema_url'}),
         name='swagger-ui'),

    #re_path(r'^swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    #re_path(r'^swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('', include('project.urls')),

]


