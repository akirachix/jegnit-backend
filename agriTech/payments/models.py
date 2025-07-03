from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
# from users.models import User


class Payment(models.Model):
    PAYMENT_TYPE_CHOICES = [
        ('farmer_to_coop', 'Farmer to Cooperative'),
        ('coop_to_supplier', 'Cooperative to Supplier'),
    ]
    payment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    payment_method = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    paid_at = models.DateTimeField()
    payment_type = models.CharField(max_length=20, choices=PAYMENT_TYPE_CHOICES)


    
    def clean(self):
        if not self.user:
            raise ValidationError("Payment must have a user associated.")
        if self.payment_type not in dict(self.PAYMENT_TYPE_CHOICES).keys():
            raise ValidationError("Invalid payment type.")

    def __str__(self):
        # if self.payment_type == 'farmer_to_coop':
            return f"{self.get_payment_type_display()}:User {self.user} has paid {self.amount}"
        # elif self.payment_type == 'coop_to_supplier':
            # return f"Cooperative {self.cooperative} paid Supplier {self.supplier} ({self.amount})"
        # return f"Payment {self.payment_id} ({self.amount})"

    class Meta:
        ordering = ['-paid_at']