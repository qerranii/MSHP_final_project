from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    height = models.IntegerField(max_length=3)
    weight = models.IntegerField(max_length=3)
    chest = models.IntegerField(max_length=3)
    waist = models.IntegerField(max_length=3)
    hips = models.IntegerField(max_length=3)
    about_me = models.CharField()

# Create your models here.
