from rest_framework import serializers
from payments.models import Payment
from tracking.models import Machinery_Tracking
from officer_visits.models import Officer_Visit
from machinery.models import Machinery
from lending_records.models import Lending_Record
from users.models import User


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Payment
#         fields = '__all__'
    # def validate_amount(self, value):
    #     if value <= 0:
    #         raise serializers.ValidationError("Amount must be positive.")
        # return value
    # def validate(self, attrs):
    #     user = attrs.get('user')
    #     payment_type = attrs.get('payment_type')
    #     farmer = attrs.get('farmer')
    #     cooperative = attrs.get('cooperative')
    #     supplier = attrs.get('supplier')
    #     if not user:
    #         raise serializers.ValidationError("Payment must have a user.")
    #     if payment_type == 'farmer_to_coop':
    #         if not farmer or not cooperative:
    #             raise serializers.ValidationError("Farmer and cooperative must be set for farmer_to_coop payment.")
    #     elif payment_type == 'coop_to_supplier':
    #         if not cooperative or not supplier:
    #             raise serializers.ValidationError("Cooperative and supplier must be set for coop_to_supplier payment.")
    #     return attrs

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields='__all__'


    def validate(self, data):
        user_type = data.get('type')
        errors = {}
        if user_type == 'cooperative' and not data.get('cooperative_name'):
            errors['cooperative_name'] = 'Required for cooperatives.'
        if user_type == 'extension_officer':
            if not data.get('officer_name'):
                errors['officer_name'] = 'Required for extension officers.'
            if not data.get('cooperative'):
                errors['cooperative'] = 'Required for extension officers.'
        if user_type == 'farmer':
            if not data.get('farmer_name'):
                errors['farmer_name'] = 'Required for farmers.'
            if not data.get('cooperative'):
                errors['cooperative'] = 'Required for farmers.'
        if user_type == 'machine_supplier' and not data.get('supplier_name'):
            errors['supplier_name'] = 'Required for machine suppliers.'
        if errors:
            raise serializers.ValidationError(errors)
        return data

class MachineryTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machinery_Tracking
        fields = '__all__'
class Officer_VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Officer_Visit
        fields = '__all__'
class MachinerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Machinery
        fields = '__all__'
class Lending_RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lending_Record
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'