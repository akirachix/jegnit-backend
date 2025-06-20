from django.db import models

# Create your models here.
class Lending_Records(models.Model):
    lending_id = models.AutoField(primary_key=True)
    machinery_id = models.ForeignKey(Machinery, on_delete=models.CASCADE)
    borrower_id = models.ForeignKey(Farmers, on_delete=models.CASCADE)
    approved_by = models.ForeignKey(Cooperatives, on_delete=models.CASCADE)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    status = models.CharField(max_length=100, null=True)