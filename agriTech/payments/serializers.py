from rest_framework import serializers
from .models import FarmerPayment, CooperativePayment

class FarmerPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmerPayment
        fields = '__all__'

class CooperativePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CooperativePayment
        fields = '__all__'
