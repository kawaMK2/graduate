from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import models as auth_models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


# Create your models here.
class Grade(models.Model):
    name = models.CharField(max_length=100)
    formal_name = models.CharField(max_length=100)
    priority = models.IntegerField()


class User(AbstractUser):
    belongs = models.ManyToManyField(Grade, through='Belong')
    objects = auth_models.UserManager()
    avatar = models.ImageField(upload_to="avatar", null=True, blank=True)
    avatar_thumbnail = ImageSpecField(source="avatar", processors=[ResizeToFill(100, 100)], format='PNG', options={'quality': 80})

    def get_full_name(self):
        self.get_username()
        return '%s %s' % (self.last_name, self.first_name)


class Belong(models.Model):
    user = models.ForeignKey(User)
    grade = models.ForeignKey(Grade)
    start_time = models.DateField()
    end_time = models.DateField(null=True, blank=True)
