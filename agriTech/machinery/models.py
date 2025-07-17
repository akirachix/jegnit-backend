from django.db import models
from users.models import User
# from users.mo import get_user_model


class Machinery(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),                                                                                                                                                                                                                                                                                                                                                                                                                                                           
        ('paid', 'Paid')
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
    





