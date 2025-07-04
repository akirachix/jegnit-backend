from django.db import models
from users.models import User

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