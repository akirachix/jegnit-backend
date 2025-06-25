from django.shortcuts import render
from rest_framework import viewsets
from machine_supplier.models import Machine_Supplier
from .serializers import MachineSupplierSerializer
# Create your views here.



class MachineSupplierViewSet(viewsets.ModelViewSet):
    queryset = Machine_Supplier.objects.all()
    serializer_class = MachineSupplierSerializer
