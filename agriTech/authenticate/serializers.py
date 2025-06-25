from rest_framework import serializers
from .models import Auth_Token

# ProductSerializer inherits from serializers.ModelSerializer
class Auth_TokenSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Auth_Token
        # says return all the fields in product
        fields = "__all__"