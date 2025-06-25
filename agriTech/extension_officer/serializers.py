from rest_framework import serializers
from .models import Extension_Officer

class ExtensionOfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extension_Officer
        fields = '__all__'


        