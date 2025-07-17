from django.db import models

# Create your models here.
class Machinery(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),                                                                                                                                                                                                                                                                                                                                                                                                                                                           
        ('paid', 'Paid')
        ]
    machinery_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    added_by = models.CharField(max_length=100, null=True)  
    created_at = models.DateTimeField()
    def __str__(self):
        return self.name
1





