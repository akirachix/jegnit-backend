from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PaymentViewSet, UserPaymentList

router = DefaultRouter()
router.register(r"", PaymentViewSet, basename='payment')

urlpatterns = [
    path("", include(router.urls)),
    path("<str:user_type>/", UserPaymentList.as_view(), name="user-payments"),
]