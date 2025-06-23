from django.db import models
from farmers.models import Farmer
from extension_officer.models import Extension_Officer

# Create your models here.
class Officer_Visit(models.Model):
    visits_id = models.AutoField(primary_key=True)
    officer_id = models.ForeignKey(Extension_Officer, on_delete=models.CASCADE)
    farmer_id = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    visit_date = models.DateTimeField()
    notes = models.TextField()