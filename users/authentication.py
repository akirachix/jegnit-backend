from django.contrib.auth.backends import BaseBackend
from users.models import Users
class Auth(BaseBackend):
    def authenticate(self, request, phone_number=None, password=None):
        try:
            user = Users.objects.get(phone_number=phone_number)
        except Users.DoesNotExist:
            return None
        if user.check_password(password):
            return user
        return None
    def get_user(self, user_id):
        try:
            return Users.objects.get(pk=user_id)
        except Users.DoesNotExist:
            return None