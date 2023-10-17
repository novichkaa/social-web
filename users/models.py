from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='images/', null=True)
    description = models.TextField(null=True)
    date = models.DateTimeField(null=True)

    def __str__(self):
        return self.username

# Create your models here.
