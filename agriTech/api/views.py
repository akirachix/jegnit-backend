from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model
User = get_user_model()

from .serializers import (
    UserSerializer,
    Lending_RecordSerializer,
    MachinerySerializer,
    Officer_VisitSerializer,
    MachineryTrackingSerializer,
    UnifiedPaymentSerializer
)
from payments.models import Payment
from lending_records.models import Lending_Record
from machinery.models import Machinery
from officer_visits.models import Officer_Visit
from tracking.models import Machinery_Tracking
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class Lending_RecordViewSet(viewsets.ModelViewSet):
    queryset = Lending_Record.objects.all()
    serializer_class = Lending_RecordSerializer
class MachineryViewSet(viewsets.ModelViewSet):
    queryset = Machinery.objects.all()
    serializer_class = MachinerySerializer
class Officer_VisitViewSet(viewsets.ModelViewSet):
    queryset = Officer_Visit.objects.all()
    serializer_class = Officer_VisitSerializer
class MachineryTrackingViewSet(viewsets.ModelViewSet):
    queryset = Machinery_Tracking.objects.all()
    serializer_class = MachineryTrackingSerializer
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = UnifiedPaymentSerializer
    permission_classes = [permissions.IsAuthenticated]