from django.db import models

class StudentResult(models.Model):
    name = models.CharField(max_length=100)
    register_number = models.CharField(max_length=15, unique=True)
    dob = models.DateField()
    subject1 = models.IntegerField()
    subject2 = models.IntegerField()
    subject3 = models.IntegerField()
    subject4 = models.IntegerField()
    subject5 = models.IntegerField()
    total = models.IntegerField()
    grade = models.CharField(max_length=2)

    def __str__(self):
        return self.register_number

class ServerStatus(models.Model):
    server_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.server_name
