from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import models as auth_models


# Create your models here.
class Grade(models.Model):
    name = models.CharField(max_length=100)
    formal_name = models.CharField(max_length=100)
    priority = models.IntegerField()


class User(AbstractUser):
    belongs = models.ManyToManyField(Grade, through='Belong')
    objects = auth_models.UserManager()


class Belong(models.Model):
    user = models.ForeignKey(User)
    grade = models.ForeignKey(Grade)
    start_time = models.DateField()
    end_time = models.DateField(null=True, blank=True)
