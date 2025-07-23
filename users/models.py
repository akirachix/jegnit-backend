from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import  User
# Create your models here.


USER_TYPE_CHOICES = [
        ('cooperative', 'Cooperative'),
        ('extension_officer', 'Extension Officer'),
        ('farmer', 'Farmer'),
        ('machine_supplier', 'Machine Supplier')]


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=30, choices=USER_TYPE_CHOICES)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(default = timezone.now)
    cooperative = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True,
        limit_choices_to={'type': 'cooperative'},
        related_name='members'
    )

   

    def __str__(self):
        return self.name or ""

       
