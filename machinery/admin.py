from django.contrib import admin
from .models import Machinery, Machinery_Tracking, Officer_Visit

@admin.register(Machinery)
class MachineryAdmin(admin.ModelAdmin):
    list_display = ('machinery_id', 'name', 'status', 'created_at', 'added_by', 'supplier_id')
    list_filter = ('status', 'created_at')
    search_fields = ('machinery_id', 'name', 'description')
    ordering = ('-created_at',)

@admin.register(Machinery_Tracking)
class MachineryTrackingAdmin(admin.ModelAdmin):
    list_display = ('tracking_id', 'machinery_id', 'latitude', 'longitude', 'timestamp')
    search_fields = ('machinery_id__machinery_id',) 
    ordering = ('-timestamp',)

@admin.register(Officer_Visit)
class OfficerVisitAdmin(admin.ModelAdmin):
    list_display = ('visits_id', 'officer_id', 'farmer_id', 'visit_date')
    search_fields = ('officer_id__phone_number', 'farmer_id__phone_number', 'notes')
    ordering = ('-visit_date',)
