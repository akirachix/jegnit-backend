from django.db import models
from django.contrib.auth.models import User


from cooperatives.models import Cooperative
# Create your models here.
class Farmer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, null = True)
    farmer_id = models.AutoField(primary_key=True)
    cooperative_id = models.ForeignKey(Cooperative, on_delete=models.CASCADE)
    farmer_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    def __str__(self):
        return self.farmer_name

