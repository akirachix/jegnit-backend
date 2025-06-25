from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MachineSupplierViewSet


router = DefaultRouter()
router.register(r"machine supplier", MachineSupplierViewSet, basename = 'machine supplier')
urlpatterns = [
    path("", include(router.urls)),
]