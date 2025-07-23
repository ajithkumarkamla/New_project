from django.db import models

# Create your models here.
from django.db import models

class StudentList(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    dob = models.DateField()
    email = models.EmailField(unique=True)

    file = models.FileField(upload_to='documents/')
    photo = models.ImageField(upload_to='photos/')

    address = models.TextField()

    def __str__(self):
        return self.name
