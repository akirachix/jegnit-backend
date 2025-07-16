from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from users.models import User




class Payment(models.Model):
    PAYMENT_TYPE_CHOICES = [
        ('farmer_to_coop', 'Farmer to Cooperative'),
        ('coop_to_supplier', 'Cooperative to Supplier'),
    ]
    PAYMENT_METHOD_CHOICES = [
        ('mobile money', 'Mobile Money'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),                                                                                                                                                                                                                                                                                                                                                                                                                                                           
        ('paid', 'Paid'),
    ]
    payment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    payment_method = models.CharField(max_length=100, choices=PAYMENT_METHOD_CHOICES)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    paid_at = models.DateTimeField()
    payment_type = models.CharField(max_length=20, choices=PAYMENT_TYPE_CHOICES)
    def clean(self):
        if not self.user:
            raise ValidationError("Payment must have a user associated.")
        if self.payment_type not in dict(self.PAYMENT_TYPE_CHOICES):
            raise ValidationError("Invalid payment type.")
        if self.amount <= 0:
            raise ValidationError("Amount must be positive.")
    class Meta:
        abstract = False
class FarmerPayment(Payment):
    farmer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'type': 'farmer'},
        related_name='farmer_payments'
    )
    cooperative = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'type': 'cooperative'},
        related_name='cooperative_farmer_payments'
    )
    def clean(self):
        super().clean()
        if self.farmer.type != 'farmer':
            raise ValidationError("The farmer must be a user of type 'farmer'.")
        if self.cooperative.type != 'cooperative':
            raise ValidationError("The cooperative must be a user of type 'cooperative'.")
    def save(self, *args, **kwargs):
        if not self.user:
            self.user = self.farmer
        super().save(*args, **kwargs)
    def __str__(self):
        return f"FarmerPayment: {self.farmer} ({self.amount})"
class CooperativePayment(Payment):
    cooperative = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'type': 'cooperative'},
        related_name='cooperative_payments'
    )
    supplier = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'type': 'machine_supplier'},
        related_name='supplier_payments'
    )
    def clean(self):
        super().clean()
        if self.cooperative.type != 'cooperative':
            raise ValidationError("The cooperative must be a user of type 'cooperative'.")
        if self.supplier.type != 'machine_supplier':
            raise ValidationError("The supplier must be a user of type 'machine_supplier'.")
    def save(self, *args, **kwargs):
        if not self.user:
            self.user = self.cooperative
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.get_payment_type_display()}: User {self.user} paid {self.amount}"
    class Meta:
        ordering = ['-paid_at']


