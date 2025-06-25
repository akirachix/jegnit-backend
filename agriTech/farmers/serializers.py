from rest_framework import serializers
from farmers.models import Farmer

# ProductSerializer inherits from serializers.ModelSerializer
class FarmerSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Farmer
        # says return all the fields in product
        fields = "__all__"