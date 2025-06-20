from django.db import models
from cooperatives.models import Cooperatives

# Create your models here.
class Farmers(models.Model):
    farmer_id = models.AutoField(primary_key=True)
    cooperative_id = models.ForeignKey(Cooperatives, on_delete=models.CASCADE)
    farmer_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    def __str__(self):
        return self.farmer_name
