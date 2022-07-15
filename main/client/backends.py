from .models import CustomUser
from django.db.models import Q
class AuthBackend(object):
    supports_object_permissions = True
    supports_object_user = False
    supports_inactive = False

    def get_user(self, user_id):
        try:
            return CustomUser.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
    
    def authenticate(self, request, username, password):
        try:
            user = CustomUser.objects.get(
                Q(username=username) | Q(email=username) | Q(phone=username)
            )
        except CustomUser.DoesNotExist:
            return None
        
        return user if user.check_password(password) else None