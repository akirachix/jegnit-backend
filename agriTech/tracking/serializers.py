from rest_framework import serializers
from .models import Machinery_Tracking


class MachineryTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machinery_Tracking
        fields = '__all__'