from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MachineryViewSet


router = DefaultRouter()
router.register('', MachineryViewSet, basename='machinery')
urlpatterns = [
    path('', include(router.urls)),
]