from django.db import models
from django.contrib.auth.models import User


class Info(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    height = models.IntegerField()
    weight = models.IntegerField()
    chest = models.IntegerField()
    waist = models.IntegerField()
    hips = models.IntegerField()
    about_me = models.CharField(max_length=300)

# Create your models here.
