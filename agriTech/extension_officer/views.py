from django.shortcuts import render
from rest_framework import viewsets
from extension_officer.models import Extension_Officer
from .serializers import ExtensionOfficerSerializer
# Create your views here.

class ExtensionOfficerViewSet(viewsets.ModelViewSet):
    queryset = Extension_Officer.objects.all()
    serializer_class = ExtensionOfficerSerializer
