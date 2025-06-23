from django.db import models
from cooperatives.models import Cooperative

# Create your models here.
class Extension_Officer(models.Model):
    extension_id = models.AutoField(primary_key=True)
    cooperative_id = models.ForeignKey(Cooperative, on_delete=models.CASCADE)
    officer_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    def __str__(self):
        return self.officer_name