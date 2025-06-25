from django.shortcuts import render
from rest_framework import viewsets
from cooperatives.models import Cooperative 
from .serializers import CooperativeSerializer

from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the AgriTech API. Use /cooperatives/, /farmers/, or /authenticate/")

# Create your views here.
class CooperativeViewSet(viewsets.ModelViewSet):
    queryset = Cooperative.objects.all()
    serializer_class = CooperativeSerializer
