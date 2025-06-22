from django.db import models
from machinery.models import Machinery

# Create your models here.

class Machinery_Tracking(models.Model):
    tracking_id = models.AutoField(primary_key=True)
    machinery_id = models.ForeignKey(Machinery, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    timestamp = models.DateTimeField()
    activity = models.TextField(null=True)
