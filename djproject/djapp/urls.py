from django.urls import path
from . import views

app_name = 'djapp'
urlpatterns = [
    path('', views.index, name='index')
]