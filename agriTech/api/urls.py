from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    Lending_RecordViewSet,
    MachineryViewSet,
    Officer_VisitViewSet,
    MachineryTrackingViewSet,
    UserViewSet,
    PaymentViewSet,
    daraja_callback,
 STKPushView,

)
router = DefaultRouter()
router.register(r"users", UserViewSet, basename='user')
router.register(r"lending-records", Lending_RecordViewSet, basename='lending_records')
router.register(r"machinery", MachineryViewSet, basename='machinery')
router.register(r"tracking", MachineryTrackingViewSet, basename='tracking')
router.register(r"officer-visits", Officer_VisitViewSet, basename='officer_visits')
router.register(r"payments", PaymentViewSet, basename='payments')

urlpatterns = [
    path("", include(router.urls)),
    path('mpesa/stk-push/', STKPushView.as_view(), name='daraja-stk-push'),
    path('mpesa/callback/', daraja_callback, name='daraja-callback'),
  
]
