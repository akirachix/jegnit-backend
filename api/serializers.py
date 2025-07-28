from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from payments.models import Payment, Lending_Record
from machinery.models import Machinery, Officer_Visit, Machinery_Tracking

User = get_user_model()  


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('phone_number', 'email', 'password', 'name', 'type', 'cooperative')

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'phone_number', 'name', 'type', 'cooperative')
        read_only_fields = ('user_id',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

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
        exclude = ['user', 'status', 'paid_at', 'checkout_request_id', 'mpesa_receipt_number']


class STKPushSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    account_reference = serializers.CharField(max_length=12, default="TX12345")
    transaction_desc = serializers.CharField()


class DarajaAPISerializer(serializers.Serializer):
    class Meta:
        model = Payment
        fields = '__all__'

    phone_number = serializers.RegexField(
        regex=r'^\+?[0-9]{10,15}$',
        error_messages={
            'invalid': 'Phone number must contain only digits and optional + at the beginning.'
        }
    )

class PhoneAuthTokenSerializer(serializers.Serializer):
    phone_number = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    token = serializers.CharField(read_only=True)

    def validate(self, attrs):
        phone_number = attrs.get('phone_number')
        password = attrs.get('password')

        if phone_number and password:
            user = authenticate(request=self.context.get('request'),
                                phone_number=phone_number, password=password)
            if not user:
                raise serializers.ValidationError("Unable to log in with provided credentials.")
        else:
            raise serializers.ValidationError("Must include 'phone_number' and 'password'.")

        attrs['user'] = user
        return attrs
