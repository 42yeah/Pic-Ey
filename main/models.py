from django.db import models

# Create your models here.
class Pic(models.Model):
    f = models.FileField()
    author = models.CharField(max_length=1024)
    name = models.CharField(max_length=1024)
    desc = models.TextField()

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=1024)
    password = models.CharField(max_length=1024)
    desc = models.TextField()
    settings_to_discover = models.BooleanField(default=False)
    settings_priv = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Comment(models.Model):
    author = models.CharField(max_length=1024)
    comment = models.TextField()
    i = models.IntegerField()

    def __str__(self):
        return self.author + '\'s comment'
