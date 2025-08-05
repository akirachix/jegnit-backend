from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken.views import obtain_auth_token


from api.views import UserRegistrationView, CustomLoginAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', CustomLoginAPIView.as_view(), name='login')
  


]