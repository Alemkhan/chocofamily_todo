from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """

    """
    def create_user(self, login, password, **extra_fields):
        if not login:
            raise ValueError("The login must be set")
        if not password:
            raise ValueError("The password must be set")

        user = self.model(login=login, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, login, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', 1)

        if extra_fields.get('role') != 1:
            raise ValueError('Superuser must have role of Global Admin')

        return self.create_user(login, password, **extra_fields)
