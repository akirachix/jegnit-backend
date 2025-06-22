from django.db import models

from cooperatives.models import Cooperative
from farmers.models import Farmer
# Create your models here.
from django.db import models
class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    payment_method = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    paid_at = models.DateTimeField()
    class Meta:
        abstract = True
class FarmerPayment(Payment):
    farmer = models.ForeignKey('farmers.Farmer', on_delete=models.CASCADE)
    cooperative = models.ForeignKey('cooperatives.Cooperative', on_delete=models.CASCADE)
    def __str__(self):
        return f"FarmerPayment: {self.farmer} ({self.amount})"
class CooperativePayment(Payment):
    cooperative = models.ForeignKey('cooperatives.Cooperative', on_delete=models.CASCADE)
    # supplier = models.ForeignKey('machine_supplier.Machine_Suppliers', on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.cooperative} -> {self.supplier} ({self.amount})"
