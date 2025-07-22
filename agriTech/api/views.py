from rest_framework import viewsets, permissions
from .serializers import (
    UserSerializer,
    Lending_RecordSerializer,
    MachinerySerializer,
    Officer_VisitSerializer,
    PaymentSerializer,
    MachineryTrackingSerializer)

from users.models import CustomUser
from payments.models import Payment
from payments.models import Lending_Record
from machinery.models import Machinery
from machinery.models import Officer_Visit
from machinery.models import Machinery_Tracking



from rest_framework import generics, permissions
from .serializers import UserRegistrationSerializer


from django.contrib.auth import get_user_model

User = get_user_model()


from rest_framework import generics, permissions, viewsets
from users.custom_user import CustomUser
from .serializers import UserRegistrationSerializer, UserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

# Registration API - anyone can register
class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.AllowAny]

# Login API - returns token + user info
class CustomLoginAPIView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.id,
            'username': user.username,
            'type': user.type
        })

# Example protected user viewset
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]




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