from django.contrib.auth import get_user_model
from django.dispatch import receiver
from corsheaders.signals import check_request_enabled


User = get_user_model()

@receiver(check_request_enabled)
def my_custom_cors_check(sender, request, **kwargs):
    """
    Enable CORS dynamically based on request or user properties.

    Example:
    - Enable CORS only for authenticated users on '/api/' paths.
    """
    user = getattr(request, 'user', None)
    if user and user.is_authenticated:
        if request.path.startswith('/api/'):
            return True
    return False

from django.conf import settings
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """
    Automatically create auth token when a new user is created.
    """
    if created:
        Token.objects.create(user=instance)

# @receiver(check_request_enabled)
# def cors_allow_api_to_specific_origins(sender, request, **kwargs):
#     # Custom logic to allow CORS requests
#     if request.path.startswith("/api/"):
#         return True
#     return False
