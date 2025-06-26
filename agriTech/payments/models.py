from django.db import models
from cooperatives.models import Cooperative
from farmers.models import Farmer
from machine_supplier.models import Machine_Supplier

class Payment(models.Model):
    PAYMENT_TYPE_CHOICES = [
        ('farmer_to_coop', 'Farmer to Cooperative'),
        ('coop_to_supplier', 'Cooperative to Supplier'),
    ]
    payment_id = models.AutoField(primary_key=True)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    payment_method = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    paid_at = models.DateTimeField()
    payment_type = models.CharField(max_length=20, choices=PAYMENT_TYPE_CHOICES)
    
    
    farmer = models.ForeignKey(Farmer, null=True, blank=True, on_delete=models.CASCADE, related_name='payments')
    cooperative = models.ForeignKey(Cooperative, null=True, blank=True, on_delete=models.CASCADE, related_name='payments')
    supplier = models.ForeignKey(Machine_Supplier, null=True, blank=True, on_delete=models.CASCADE, related_name='payments')

    def clean(self):
        from django.core.exceptions import ValidationError

        if self.payment_type == 'farmer_to_coop':
            if not self.farmer or not self.cooperative or self.supplier:
                raise ValidationError("Farmer to Cooperative payments must have farmer and cooperative set, supplier must be null.")
        
        elif self.payment_type == 'coop_to_supplier':
            if not self.cooperative or not self.supplier or self.farmer:
                raise ValidationError("Cooperative to Supplier payments must have cooperative and supplier set, farmer must be null.")
        else:
            raise ValidationError("Invalid payment type.")

    def __str__(self):
        if self.payment_type == 'farmer_to_coop':
            return f"Farmer {self.farmer} paid Cooperative {self.cooperative} ({self.amount})"
        elif self.payment_type == 'coop_to_supplier':
            return f"Cooperative {self.cooperative} paid Supplier {self.supplier} ({self.amount})"
        return f"Payment {self.payment_id} ({self.amount})"

    class Meta:
        ordering = ['-paid_at']