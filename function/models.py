from asyncio.windows_events import NULL
from email.policy import default
from unicodedata import name
from django.db import models
from matplotlib import image

# Create your models here.
class formsubmit(models.Model):
    photo = models.FileField(null = False,blank= False,upload_to="useruploads",default= NULL)
    description = models.TextField(max_length=1000)
    location = models.CharField(max_length=100)
    journeyname = models.TextField(max_length=20)
    date = models.DateField()


class userjourneydata(models.Model):
    name = models.TextField(max_length=40,default = NULL)
    personimage = models.ImageField(default = NULL)
    photo = models.FileField()
    description = models.TextField(max_length=1000)
    journeylocation = models.CharField(max_length=50,default=NULL)
    placelocation = models.CharField(max_length=200,default=NULL)
    journeyname = models.TextField(max_length=30)
    date = models.DateField()
    key = models.IntegerField(default=NULL)
    keyid = models.IntegerField(default=NULL)

class comments(models.Model):
    key = models.IntegerField(default=NULL)
    comments = models.TextField(max_length=1000)