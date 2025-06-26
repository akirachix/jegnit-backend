
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from officer_visits.models import Officer_Visit
from .serializers import Officer_VisitSerializer

class Officer_VisitViewSet(viewsets.ModelViewSet):
    queryset = Officer_Visit.objects.all()
    serializer_class = Officer_VisitSerializer