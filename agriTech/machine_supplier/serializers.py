from rest_framework import serializers
from .models import Machine_Supplier

class MachineSupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine_Supplier
        fields = '__all__'
