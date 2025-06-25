from rest_framework import viewsets
from .models import FarmerPayment, CooperativePayment
from .serializers import FarmerPaymentSerializer, CooperativePaymentSerializer

class FarmerPaymentViewSet(viewsets.ModelViewSet):
    queryset = FarmerPayment.objects.all()
    serializer_class = FarmerPaymentSerializer

class CooperativePaymentViewSet(viewsets.ModelViewSet):
    queryset = CooperativePayment.objects.all()
    serializer_class = CooperativePaymentSerializer