from django.db import models
from users.models import User
# Create your models here.


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    payment_method = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    paid_at = models.DateTimeField()
    class Meta:
        abstract = True
class FarmerPayment(Payment):
    farmer = models.ForeignKey(User,
        on_delete=models.CASCADE,
        limit_choices_to={'type': 'farmer'},
        related_name='farmer_payments')
    cooperative = models.ForeignKey(User,
        on_delete=models.CASCADE,
        limit_choices_to={'type': 'cooperative'},
        related_name='cooperative_farmer_payments')
    def __str__(self):
        return f"FarmerPayment: {self.farmer} ({self.amount})"
class CooperativePayment(Payment):
    cooperative = models.ForeignKey(User,
        on_delete=models.CASCADE,
        limit_choices_to={'type': 'cooperative'},
        related_name='cooperative_payments')
    supplier = models.ForeignKey( User,
        on_delete=models.CASCADE,
        limit_choices_to={'type': 'machine_supplier'},
        related_name='supplier_payments')
    def __str__(self):
        return f"{self.cooperative} -> {self.supplier} ({self.amount})"
