from django.db import models
from extension_officer.models import Extension_Officers

# Create your models here.
class Officer_Visits(models.Model):
    visits_id = models.AutoField(primary_key=True)
    officer_id = models.ForeignKey(Extension_Officers, on_delete=models.CASCADE)
    farmer_id = models.ForeignKey(Farmers, on_delete=models.CASCADE)
    visit_date = models.DateTimeField()
    notes = models.TextField()

