from django.db import models
# Create your models here.

class Person(models.Model):
	first_name = models.CharField(max_length=30)
	Last_name = models.CharField(max_length=30)

def __unicode__(self):
        return '%s' %self.title
