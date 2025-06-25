from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Auth_TokenViewSet



router = DefaultRouter()
router.register(r"authentication", Auth_TokenViewSet, basename = "authentication")

urlpatterns = [
    path("", include(router.urls)),

]