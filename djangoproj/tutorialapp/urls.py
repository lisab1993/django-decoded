from rest_framework import routers
from django.urls import path, include
from tutorialapp import views
from . views import StepView

# router = routers.DefaultRouter()
# router.register(r'tutorialapp', views.StepViewSet, basename='tutorialapp')


urlpatterns = [
    # path('', include(router.urls)),
    path('', StepView.as_view(), name='step_view')
]