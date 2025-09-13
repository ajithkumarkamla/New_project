from django.db import models

# Create your models here.
class Userdata(models.Model):
    name= models.CharField(max_length=100)
    age=models.IntegerField()
