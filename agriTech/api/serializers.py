from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



    def validate(self, data):
        user_type = data.get('type')
        errors = {}
        if user_type == 'cooperative' and not data.get('cooperative_name'):
            errors['cooperative_name'] = 'This field is required for cooperatives.'
        if user_type == 'extension_officer':
            if not data.get('officer_name'):
                errors['officer_name'] = 'This field is required for extension officers.'
            if not data.get('cooperative'):
                errors['cooperative'] = 'This field is required for extension officers.'
        if user_type == 'farmer':
            if not data.get('farmer_name'):
                errors['farmer_name'] = 'This field is required for farmers.'
            if not data.get('cooperative'):
                errors['cooperative'] = 'This field is required for farmers.'
        if user_type == 'machine_supplier' and not data.get('supplier_name'):
            errors['supplier_name'] = 'This field is required for machine suppliers.'
        if errors:
            raise serializers.ValidationError(errors)
        return data
  