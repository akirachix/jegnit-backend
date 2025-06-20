from django.db import models

# Create your models here.
class Auth_Tokens(models.Model):
    tokens_id = models.AutoField(primary_key=True)
    token = models.CharField(max_length=100)
    expired_at = models.DateTimeField()
