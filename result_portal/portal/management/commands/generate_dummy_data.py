from django.core.management.base import BaseCommand
from portal.models import Student, Result
from faker import Faker
import random

class Command(BaseCommand):
    help = "Creates 200 unique fake students & results"

    def handle(self, *args, **kwargs):
        fake = Faker()
        Student.objects.all().delete()
        Result.objects.all().delete()

        existing_regs = set()

        for _ in range(200):
            # Generate unique register number
            while True:
                reg = f"22CS{random.randint(1000, 1999)}"
                if reg not in existing_regs:
                    existing_regs.add(reg)
                    break

            dob = fake.date_of_birth(minimum_age=17, maximum_age=22)
            student = Student.objects.create(register_number=reg, dob=dob)
            Result.objects.create(
                student=student,
                semester=random.randint(1, 8),
                gpa=round(random.uniform(6.0, 10.0), 2)
            )

        self.stdout.write(self.style.SUCCESS("✅ Unique dummy data generated successfully!"))
