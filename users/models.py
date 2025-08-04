from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

from django.contrib.auth import get_user_model




USER_TYPE_CHOICES = [
    ('cooperative', 'Cooperative'),
    ('extension_officer', 'Extension Officer'),
    ('farmer', 'Farmer'),
    ('machine_supplier', 'Machine Supplier'),
]

class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('The phone number must be set')
        
        phone_number = phone_number.strip()

        user_type = extra_fields.get('type', None)
        if user_type == 'cooperative':
            extra_fields.setdefault('is_staff', True)
            extra_fields.setdefault('is_superuser', True)
            extra_fields.setdefault('is_active', True)

        user = self.model(phone_number=phone_number, **extra_fields)
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('type', 'cooperative')
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('type') != 'cooperative':
            raise ValueError('Superuser must be of type cooperative.')

        return self.create_user(phone_number, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=20, unique=True)
    type = models.CharField(max_length=30, choices=USER_TYPE_CHOICES)
    name = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True, blank=True, null=True)
    cooperative = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={'type': 'cooperative'},
        related_name='members'
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['type']  

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.name or f"{self.get_type_display()} ({self.phone_number})"



class CooperativeUserManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type='cooperative')

class CooperativeUser(CustomUser):
    objects = CooperativeUserManager()

    class Meta:
        proxy = True
        verbose_name = 'Cooperative (Admin) User'
        verbose_name_plural = 'Cooperative (Admin) Users'



class ExtensionOfficerManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type='extension_officer')

class ExtensionOfficerUser(CustomUser):
    objects = ExtensionOfficerManager()

    class Meta:
        proxy = True
        verbose_name = 'Extension Officer User'
        verbose_name_plural = 'Extension Officer Users'


class FarmerManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type='farmer')

class FarmerUser(CustomUser):
    objects = FarmerManager()

    class Meta:
        proxy = True
        verbose_name = 'Farmer User'
        verbose_name_plural = 'Farmer Users'


class MachineSupplierManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type='machine_supplier')

class MachineSupplierUser(CustomUser):
    objects = MachineSupplierManager()

    class Meta:
        proxy = True
        verbose_name = 'Machine Supplier User'
        verbose_name_plural = 'Machine Supplier Users'
