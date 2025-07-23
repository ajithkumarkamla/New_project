from django.db import models

class Student(models.Model):
    register_number = models.CharField(max_length=20, unique=True)
    dob             = models.DateField()

    def __str__(self):
        return self.register_number


class Result(models.Model):
    student  = models.OneToOneField(Student, on_delete=models.CASCADE)
    semester = models.PositiveSmallIntegerField()
    gpa      = models.DecimalField(max_digits=4, decimal_places=2)
    updated  = models.DateTimeField(auto_now=True)
