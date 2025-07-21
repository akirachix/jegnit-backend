from rest_framework import serializers
from payments.models import Payment
# from tracking.models import Machinery_Tracking
# from officer_visits.models import Officer_Visit
from machinery.models import Machinery
# from lending_records.models import Lending_Record
from payments.models import Payment
from machinery.models import Machinery_Tracking
from machinery.models import Officer_Visit
from machinery.models import Machinery
from payments.models import Lending_Record
from users.models import User
from .mpesa import DarajaAPI





class UserSerializer(serializers.ModelSerializer):
    cooperative_name = serializers.CharField(required=False, allow_blank=True)
    officer_name = serializers.CharField(required=False, allow_blank=True)
    farmer_name = serializers.CharField(required=False, allow_blank=True)
    supplier_name = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ['user_id',
        'type',
        'email',
        'password',
        'phone_number',
        'created_at',
        'last_login',
        'date_joined',
        'cooperative_name',
        'officer_name',
        'farmer_name',
        'supplier_name',
        'cooperative',
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }
        fields='__all__'


    def validate(self, data):
        user_type = data.get('type')
        errors = {}

        if user_type == 'cooperative' and not data.get('cooperative_name'):
            errors['cooperative_name'] = 'Required for cooperatives.'
        if user_type == 'extension_officer':
            if not data.get('officer_name'):
                errors['officer_name'] = 'Required for extension officers.'
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

class STKPushSerializer(serializers.Serializer):
   phone_number = serializers.CharField()
   amount = serializers.DecimalField(max_digits=10, decimal_places=2)
   account_reference = serializers.CharField(max_length=12, default="TX12345")
   transaction_desc = serializers.CharField()
class DarajaAPISerializer(serializers.Serializer):
   class Meta:
       model= Payment
       fields= '__all__'
       phone_number = serializers.RegexField(
        regex = r'^\+?[0-9]{10,15}$',
        error_messages = {'invalid':
        'Phone number must contain only digits and optional + at the beginning.'}
    )

