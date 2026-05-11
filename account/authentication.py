from django.contrib.auth import get_user_model
from .models import Profile

class EmailAuthBackend:
    """
    Authenticate using either a username or an e-mail address.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        if username is None or password is None:
            return None

        try:
            user = UserModel.objects.get(email__iexact=username)
        except (UserModel.DoesNotExist, UserModel.MultipleObjectsReturned):
            try:
                user = UserModel.objects.get(username__iexact=username)
            except (UserModel.DoesNotExist, UserModel.MultipleObjectsReturned):
                return None

        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None


def create_profile(backend, user, *args, **kwargs):
    """
    Create a user profile for social authentication users.
    """
    if user:
        Profile.objects.get_or_create(user=user)
