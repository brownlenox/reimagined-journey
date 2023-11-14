import json
from django.core.management.base import BaseCommand

import os.path
from NewClass import settings
from mainapp.models import Employee

class Command(BaseCommand):
    help = "Populates employees table with 1000 records"

    def handle(self, *args, **options):
        path = os.path.join(settings.BASE_DIR, "employees.json")
        self.stdout.write(
            self.style.SUCCESS("Started to import data")
        )
        with open(path) as file:  # file = open(path)
            employees = json.load(file)
            for e in employees:
                Employee.objects.create(
                    name=e['name'],
                    email=e['email'],
                    dob=e['dob'],
                    salary=e['salary'],
                    disabled=e["disbled"],
                )

        self.stdout.write(
            self.style.SUCCESS("Completed  importing data")
        )

        # celery tasks