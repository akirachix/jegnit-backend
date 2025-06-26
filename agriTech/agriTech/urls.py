
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path("officer_visits/", include("officer_visits.urls")),
    path("lending_records/", include("lending_records.urls")),


    path('extension_officer/', include('extension_officer.urls')),
    path('api/', include('extension_officer.urls')),
    path('machine_supplier/', include('machine_supplier.urls')),
    path('api/', include('machine_supplier.urls')),
    path('machinery/', include('machinery.urls')), 
    path('tracking/', include('tracking.urls')), 


]
