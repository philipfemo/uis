from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password = None,):
        if not email:
            raise ValueError('Users must provide email')

        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
        )

        user.set_password(password)
        user.save(using = self._db)
        return user
