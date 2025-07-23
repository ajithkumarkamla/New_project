from django.core.management.base import BaseCommand
from faker import Faker
from portal.models import Student, Result
import random

class Command(BaseCommand):
    help = "Create 200 unique fake students & results"

    def handle(self, *args, **kwargs):
        fake = Faker()
        Student.objects.all().delete()
        Result.objects.all().delete()
        regs = set()
        while len(regs) < 200:
            reg = f"22CS{random.randint(1000,1999)}"
            if reg in regs: continue
            regs.add(reg)
            dob = fake.date_of_birth(minimum_age=17, maximum_age=22)
            s   = Student.objects.create(register_number=reg, dob=dob)
            Result.objects.create(student=s,
                                  semester=random.randint(1,8),
                                  gpa=round(random.uniform(6.0,10.0),2))
        self.stdout.write(self.style.SUCCESS("Dummy data ready!"))
