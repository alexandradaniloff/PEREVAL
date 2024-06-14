from django.urls import path, include, re_path
from django.contrib import admin
from rest_framework import routers, permissions
from project import views
from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



router = routers.DefaultRouter()
router.register(r'users', views.UsersViewset, basename='users')
router.register(r'coords', views.CoordsViewset, basename='coords')
router.register(r'levels', views.LevelViewset, basename='levels')
router.register(r'images', views.ImagesViewset, basename='images')
router.register(r'perevals', views.PerevalViewset, basename='perevals')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    #path('api-auth/', UsersViewset.as_view({'get': 'list'}))


]