from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Machinery
from .serializers import MachinerySerializer


class MachineryViewSet(viewsets.ModelViewSet):
    queryset = Machinery.objects.all()
    serializer_class = MachinerySerializer