from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    city = models.CharField(max_length=100, blank=True, default="")
    city2 = models.CharField(max_length=100, blank=True, default="")
    city3 = models.CharField(max_length=100, blank=True, default="")
    city4 = models.CharField(max_length=100, blank=True, default="")
    city5 = models.CharField(max_length=100, blank=True, default="")
