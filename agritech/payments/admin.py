from django.contrib import admin
from .models import FarmerPayment, CooperativePayment

admin.site.register(FarmerPayment)
admin.site.register(CooperativePayment)