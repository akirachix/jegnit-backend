from django.db import models, transaction
import re


class Machinery(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('in_use', 'In Use'),
    ]

    machinery_id = models.CharField(primary_key=True, max_length=20, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    image=models.URLField(max_length=500, blank=True, null=True) 
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(
        'users.CustomUser', on_delete=models.CASCADE, related_name='machineries_added',
        limit_choices_to={'type__in': ['cooperative', 'machine_supplier']}
    )
    supplier_id = models.ForeignKey(
        'users.CustomUser', on_delete=models.CASCADE, related_name='machineries_supplied',
        null=True, limit_choices_to={'type': 'machine_supplier'}
    )

    def generate_prefix(self):
        words = re.findall(r'\b\w', self.name.upper())
        return ''.join(words)[:3]

    def save(self, *args, **kwargs):
        if not self.machinery_id:
            prefix = self.generate_prefix()
            with transaction.atomic():
                last_id = (
                    Machinery.objects
                    .filter(machinery_id__startswith=prefix)
                    .order_by('-machinery_id')
                    .first()
                )
                if last_id:
                    last_num = int(last_id.machinery_id.replace(prefix, ''))
                    next_num = last_num + 1
                else:
                    next_num = 1
                self.machinery_id = f"{prefix}{next_num:03d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.machinery_id} - {self.name}"


class Machinery_Tracking(models.Model):
    tracking_id = models.AutoField(primary_key=True)
    machinery_id = models.ForeignKey(Machinery, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    timestamp = models.DateTimeField()
    activity = models.TextField(null=True)


class Officer_Visit(models.Model):
    visits_id = models.AutoField(primary_key=True)
    officer_id = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.CASCADE,
        limit_choices_to={'type': 'extension_officer'},
        related_name='officer_visits'
    )
    farmer_id = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.CASCADE,
        limit_choices_to={'type': 'farmer'},
        related_name='farmer_visits'
    )
    visit_date = models.DateTimeField()
    notes = models.TextField()
