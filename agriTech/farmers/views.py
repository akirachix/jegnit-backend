from django.shortcuts import render
from rest_framework import viewsets
from farmers.models import Farmer
from .serializers import FarmerSerializer

# Create your views here.
class FarmerViewSet(viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer