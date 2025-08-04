from rest_framework import viewsets, generics, permissions, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model, authenticate

from .serializers import (
    UserRegistrationSerializer,
    CustomUserSerializer,
    UserSerializer,
    Lending_RecordSerializer,
    MachinerySerializer,
    Officer_VisitSerializer,
    PaymentSerializer,
    MachineryTrackingSerializer,
    STKPushSerializer,
    PhoneAuthTokenSerializer,
)

from .serializers import PhoneAuthTokenSerializer
from payments.models import Payment, Lending_Record
from machinery.models import Machinery, Officer_Visit, Machinery_Tracking
from users.models import CustomUser
from .mpesa import DarajaAPI

User = get_user_model()


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.AllowAny]

class CustomLoginAPIView(ObtainAuthToken):
    serializer_class = PhoneAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.user_id,
            'phone_number': user.phone_number,
            'type': user.type,
            'name': user.name,
        })


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
    serializer_class = PaymentSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Payment.objects.filter(status='in-progress')

    def perform_create(self, serializer):
        serializer.save()


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
