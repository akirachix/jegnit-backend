from django.contrib import admin

# Register your models here.
from .models import FarmerPayment, CooperativePayment
admin.site.register(FarmerPayment)
admin.site.register(CooperativePayment)
