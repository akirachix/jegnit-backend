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
    class Meta:
        model = User
        fields = ['user_id',
        'type',
        'name',
        'email',
        'password',
        'phone_number',
        'created_at',
        'last_login',
        'date_joined',
        'cooperative',
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }
        fields='__all__'


    def validate(self, data):
        user_type = data.get('type')
        errors = {}

        if user_type == 'cooperative' and data.get('cooperative'):
            errors['cooperative'] = 'Cooperative users should not be linked to another cooperative.'

        if user_type in ['extension_officer', 'farmer'] and not data.get('cooperative'):
            errors['cooperative'] = f'Cooperative is required for {user_type.replace("_", " ")}.'

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
        exclude = ['user', 'status' ,'paid_at', 'checkout_request_id', 'mpesa_receipt_number']

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

