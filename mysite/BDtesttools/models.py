from __future__ import unicode_literals

from django.db import models


#Create your models here
class Usersinfo(models.Model):
    appid=models.CharField(max_length=20)
    uid=models.CharField(max_length=30)
    actionid=models.CharField(max_length=3)
    itemtype=models.CharField(max_length=3)
    utype=models.CharField(max_length=3)
