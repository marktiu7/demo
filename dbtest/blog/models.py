from __future__ import unicode_literals

from django.db import models

# Create your models here.
class picinfo(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    date =models.DateTimeField()


class userinfo(models.Model):
     name = models.CharField(max_length=30)
     email = models.EmailField()
     memo = models.TextField()

     
   #  def __unicode__(self):
    #     return self.name