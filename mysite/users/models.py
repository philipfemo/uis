from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager
# Create your models here.
class User(AbstractBaseUser):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    ##password = models.CharField(max_length=128)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUEIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return (self.email)
