from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
path('cooperatives/', include('cooperatives.urls')),
     path('farmers/', include('farmers.urls')),
     path('authenticate/', include('authenticate.urls')),
]
