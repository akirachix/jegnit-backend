from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FarmerPaymentViewSet, CooperativePaymentViewSet

router = DefaultRouter()
router.register(r"farmer-payments", FarmerPaymentViewSet, basename='farmer-payment')
router.register(r"cooperative-payments", CooperativePaymentViewSet, basename='cooperative-payment')

urlpatterns = [
    path("", include(router.urls)),
]