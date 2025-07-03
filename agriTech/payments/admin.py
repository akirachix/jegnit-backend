
from django.contrib import admin
from .models import Payment

admin.site.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'payment_id',
        'payment_type',
        'amount',
        'status',
        'paid_at',
        'user_id',
    )
    list_filter = ('payment_type', 'status', 'cooperative', 'supplier', 'farmer')
    search_fields = ('payment_id', 'farmer__name', 'cooperative__name', 'supplier__name')
    ordering = ('-paid_at',)