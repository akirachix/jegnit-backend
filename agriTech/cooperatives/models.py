from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Cooperative(models.Model):
    user = models.OneToOneField (User, on_delete = models.CASCADE, null = True)
    cooperative_id = models.AutoField(primary_key=True)
    cooperative_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    def __str__(self):
        return self.cooperative_name


