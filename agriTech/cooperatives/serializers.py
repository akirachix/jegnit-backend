from rest_framework import serializers
from cooperatives.models import Cooperative

# ProductSerializer inherits from serializers.ModelSerializer
class CooperativeSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Cooperative
        # says return all the fields in product
        fields = "__all__"