from django.contrib import admin

from .models import Payment
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'payment_id',
        'payment_type',
        'amount',
        'status',
        'paid_at',
        'user',
        'get_party',
    )
    list_filter = ('payment_type', 'status')
    search_fields = ('payment_id', 'user__username')
    ordering = ('-paid_at',)
    def get_party(self, obj):
        if hasattr(obj, 'farmerpayment'):
            return f"{obj.farmerpayment.farmer} → {obj.farmerpayment.cooperative}"
        elif hasattr(obj, 'cooperativepayment'):
            return f"{obj.cooperativepayment.cooperative} → {obj.cooperativepayment.supplier}"
        return "-"
    get_party.short_description = 'Party'
