from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .forms import CustomUserCreationForm  # your custom creation form with 4-digit password
from .models import CustomUser

class CustomUserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserCreationForm
    model = CustomUser

    list_display = ('phone_number', 'name', 'type', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'type')

    search_fields = ('phone_number', 'name')
    ordering = ('name',)

    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        (_('Personal info'), {'fields': ('name', 'type', 'cooperative')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'password', 'name', 'type', 'cooperative'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
