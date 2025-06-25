
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from lending_records.models import Lending_Record
from .serializers import Lending_RecordSerializer

class Lending_RecordViewSet(viewsets.ModelViewSet):
    queryset = Lending_Record.objects.all()
    serializer_class = Lending_RecordSerializer
