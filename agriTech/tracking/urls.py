from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MachineryTrackingViewSet


router = DefaultRouter()
router.register('', MachineryTrackingViewSet, basename='tracking')
urlpatterns = [
    path('', include(router.urls)),
]