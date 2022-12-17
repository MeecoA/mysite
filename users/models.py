from django.db import models
from django.contrib.auth.models import AbstractUser, User
from users.managers import UserManager

# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=50, unique=True)
    role = models.CharField(max_length=12, default="", error_messages={
    'required': "Role must be provided"
    })
    department = models.CharField(max_length=10, blank=True, null=True, default="")


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __unicode__(self):
        return self.email

    objects = UserManager()