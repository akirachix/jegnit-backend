# users/custom_user.py

from django.contrib.auth.models import AbstractUser
from django.db import models

USER_TYPE_CHOICES = [
    ('cooperative', 'Cooperative'),
    ('extension_officer', 'Extension Officer'),
    ('farmer', 'Farmer'),
    ('machine_supplier', 'Machine Supplier'),
]

class CustomUser(AbstractUser):
    type = models.CharField(max_length=30, choices=USER_TYPE_CHOICES)
    cooperative_name = models.CharField(max_length=100, blank=True, null=True)
    officer_name = models.CharField(max_length=100, blank=True, null=True)
    cooperative = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True,
        limit_choices_to={'type': 'cooperative'},
        related_name='members'
    )
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    farmer_name = models.CharField(max_length=100, blank=True, null=True)
    supplier_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        if self.type == 'cooperative':
            display = self.cooperative_name or "Unnamed Cooperative"
        elif self.type == 'extension_officer':
            display = self.officer_name or "Unnamed Officer"
        elif self.type == 'farmer':
            display = self.farmer_name or "Unnamed Farmer"
        elif self.type == 'machine_supplier':
            display = self.supplier_name or "Unnamed Supplier"
        else:
            display = "Unknown User"
        return f"{display} ({self.get_type_display()})"
