from rest_framework import viewsets, generics
from .models import Payment
from .serializers import PaymentSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class UserPaymentList(generics.ListAPIView):
    serializer_class = PaymentSerializer

    def get_queryset(self):
        user_type = self.kwargs.get("user_type")
        if user_type == "farmer":
            return Payment.objects.filter(payment_type='farmer_to_coop')
        elif user_type == "cooperative":
            return Payment.objects.filter(payment_type__in=['farmer_to_coop', 'coop_to_supplier'])
        elif user_type == "supplier":
            return Payment.objects.filter(payment_type='coop_to_supplier')
        else:
            return Payment.objects.none()