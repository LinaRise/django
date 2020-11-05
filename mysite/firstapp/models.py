from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Students(models.Model):
    group = models.CharField(max_length=10)
    lastname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    interests = models.TextField()

    def __str__(self):
        return self.group
