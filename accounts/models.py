from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    photo = models.ImageField(upload_to='users', null=True, blank=True)
    email = models.EmailField(unique=True)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", 'first_name']
