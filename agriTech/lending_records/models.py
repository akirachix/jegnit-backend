from django.db import models
from users.models import User
from machinery.models import Machinery
# Create your models here.
class Lending_Record(models.Model):
    lending_id = models.AutoField(primary_key=True)
    machinery_id = models.ForeignKey(Machinery, on_delete=models.CASCADE)
    borrower = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'type': 'farmer'})
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='approved_lendings', limit_choices_to={'type': 'cooperative'})
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    status = models.CharField(max_length=100, null=True)
