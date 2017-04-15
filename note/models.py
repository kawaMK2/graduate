from django.db import models
from accounts.models import User


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    locate = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    elapsed_time = models.IntegerField()
    user = models.ForeignKey(User)
    tag = models.ManyToManyField(Tag)
    text_type = models.IntegerField()
    has_metadata = models.BooleanField(default=False)


class Comment(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    note = models.ForeignKey(Note)
    posted_date = models.DateTimeField()
