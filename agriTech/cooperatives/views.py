from django.shortcuts import render
from rest_framework import viewsets
from cooperatives.models import Cooperative 
from .serializers import CooperativeSerializer


# Create your views here.
class CooperativeViewSet(viewsets.ModelViewSet):
    queryset = Cooperative.objects.all()
    serializer_class = CooperativeSerializer
