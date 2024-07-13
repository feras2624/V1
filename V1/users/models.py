from django.db import models
from django.contrib.auth.models import AbstractUser


class Cuser(AbstractUser):
    email = models.EmailField(max_length=100,unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
