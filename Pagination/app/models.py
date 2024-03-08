from django.db import models

# Create your models here.
class School(models.Model):
    Sname = models.CharField(max_length=200)
    Saddress = models.CharField(max_length=200)
    Scode = models.IntegerField()
