from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Auth_TokenViewSet



router = DefaultRouter()
router.register(r"autt_token", Auth_TokenViewSet, basename = "auth_token")

urlpatterns = [
    path("", include(router.urls)),

]