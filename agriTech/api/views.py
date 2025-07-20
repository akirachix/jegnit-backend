from rest_framework import viewsets, permissions
from .serializers import (
    UserSerializer,
    Lending_RecordSerializer,
    MachinerySerializer,
    Officer_VisitSerializer,
    PaymentSerializer,
    MachineryTrackingSerializer)


from users.models import User
from payments.models import Payment
from lending_records.models import Lending_Record
from machinery.models import Machinery
from officer_visits.models import Officer_Visit
from tracking.models import Machinery_Tracking
from rest_framework import status
from .mpesa import DarajaAPI
from .serializers import STKPushSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response


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
    serializer_class = PaymentSerializer
    permission_classes = [permissions.AllowAny]
class STKPushView(APIView):
    def post(self, request):
        serializer = STKPushSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            daraja = DarajaAPI()
            response = daraja.stk_push(
                phone_number=data['phone_number'],
                amount=data['amount'],
                account_reference=data['account_reference'],
                transaction_desc=data['transaction_desc']
            )
            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def daraja_callback(request):
    print("Daraja Callback Data:", request.data)
    return Response({"ResultCode": 0, "ResultDesc": "Accepted"})