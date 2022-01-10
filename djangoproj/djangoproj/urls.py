from django.urls import include, path
from rest_framework import routers
from tutorialapp.views import StepViewSet
from tutorialapp import views

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.shortcuts import render

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='Users')
router.register(r'groups', views.GroupViewSet, basename='Groups')
router.register(r'Step/', views.StepViewSet, basename='Step')

vue_urls = [
  path('', lambda request: HttpResponse(render(request, 'vue_index.html'))),
  path('another-path/', lambda request: HttpResponse(render(request, 'vue_index.html'))),
]

urlpatterns = [
    path('router/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('api/', include('tutorialapp.urls')),
    path('', include(vue_urls))
]



