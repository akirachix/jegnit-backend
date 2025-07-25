from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Machinery(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),                                                                                                                                                                                                                                                                                                                                                                                                                                                           
        ('In_use', 'in_use')
        ]

        
        
    machinery_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)  
    created_at = models.DateTimeField()

    added_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='machineries_added',limit_choices_to={'type__in': ['cooperative', 'machine_supplier']})
    supplier_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='machineries_supplied',null=True,limit_choices_to={'type': 'machine_supplier'})

    def __str__(self):
        return self.name
    




class Machinery_Tracking(models.Model):
    tracking_id = models.AutoField(primary_key=True)
    machinery_id = models.ForeignKey(Machinery, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    timestamp = models.DateTimeField()
    activity = models.TextField(null=True)



# Create your models here.
class Officer_Visit(models.Model):
    visits_id = models.AutoField(primary_key=True)
    officer_id = models.ForeignKey(User,
        on_delete=models.CASCADE,
        limit_choices_to={'type': 'extension_officer'},
        related_name='officer_visits')
    farmer_id = models.ForeignKey( User,
        on_delete=models.CASCADE,
        limit_choices_to={'type': 'farmer'},
        related_name='farmer_visits')
    visit_date = models.DateTimeField()
    notes = models.TextField()