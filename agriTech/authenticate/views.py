from django.shortcuts import render
from rest_framework import viewsets
from .models import Auth_Token 
from .serializers import Auth_TokenSerializer

# Create your views here.
class Auth_TokenViewSet(viewsets.ModelViewSet):
    queryset = Auth_Token.objects.all()
    serializer_class = Auth_TokenSerializer