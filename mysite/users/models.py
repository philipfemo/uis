from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager
# Create your models here.
class User(AbstractBaseUser):
    HUMANISTISK = 'HU'
    JURIDISK = 'JU'
    NATURVID = 'NV'
    SAMFUNDVID = 'SAV'
    SUNDHEDVID = 'SUV'
    TEOLOGISK = 'TE'
    FACULTY_CHOICES = (
        (HUMANISTISK, 'Humanistisk Fakultet'),
        (JURIDISK, 'Juridisk Fakultet'),
        (NATURVID, 'Naturvidenskabelige Fakultet'),
        (SAMFUNDVID, 'Samfundsvidenskabelige Fakultet'),
        (SUNDHEDVID, 'Sundhedsvidenskabelige Fakultet'),
        (TEOLOGISK, 'Teologiske Fakultet'),
    )

    STUDERENDE = 'S'
    PROFESSOR = 'P'

    ROLES_CHOICES = (
        (STUDERENDE, 'Studerende'),
        (PROFESSOR, 'Professor'),
    )

    roles = models.CharField(
        max_length = 3,
        choices = ROLES_CHOICES,
        default = STUDERENDE,
    )
    faculty = models.CharField(
        max_length = 3,
        choices = FACULTY_CHOICES,
        default = HUMANISTISK,
    )
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    #password = models.CharField(max_length=128)
    study = models.CharField(max_length=128)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUEIRED_FIELDS = ['first_name', 'last_name', 'faculty', 'study', 'roles']

    def __str__(self):
        return (self.email)
