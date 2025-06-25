from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExtensionOfficerViewSet


router = DefaultRouter()
router.register(r"extension officer", ExtensionOfficerViewSet, basename = 'extension officer')
urlpatterns = [
    path("", include(router.urls)),
]