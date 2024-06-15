
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from django.urls import path, include, re_path
from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger-ui',
         TemplateView.as_view(template_name='flatpages/swagger-ui.html', extra_context={'schema_url': 'schema_url'}),
         name='swagger-ui'),

    #re_path(r'^swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    #re_path(r'^swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('', include('project.urls')),

]


