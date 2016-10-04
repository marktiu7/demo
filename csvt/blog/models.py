from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=100)
    email = models.EmailField()
    
    def __unicode__(self):
        return self.username