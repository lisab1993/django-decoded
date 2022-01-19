from rest_framework import routers
from django.urls import path, include
from tutorialapp import views
from . views import StepView, PageView

# router = routers.DefaultRouter()
# router.register(r'tutorialapp', views.StepViewSet, basename='tutorialapp')


urlpatterns = [
    # path('', include(router.urls)),
    path('step/', StepView.as_view(), name='step_view'),
    path('page/', PageView.as_view(), name='page_view'),
]