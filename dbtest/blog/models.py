from __future__ import unicode_literals

from django.db import models

class Commoninfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    class Meta:
        abstract = True


class Student(Commoninfo):
    home_group = models.CharField(max_length=50)

    class Meta(Commoninfo.Meta):
        db_table='Student'

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