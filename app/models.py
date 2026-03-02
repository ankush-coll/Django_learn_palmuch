from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Members(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)


class Songs(models.Model):
    title=models.CharField(max_length=255)
    youtube_url=models.URLField()
    release_year=models.DateField()

class EmailOTP(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    otphash=models.CharField(max_length=128)
    created_at=models.DateTimeField(auto_now_add=True)
    attempts=models.IntegerField(default=0)

class SiteVisit(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    