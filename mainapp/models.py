from django.db import models
import uuid
import os

def unique_img_name(instance, filename):
    name = uuid.uuid4()
    ext = filename.split(".")[-1]
    full_name = f"{name}.{ext}"
    # full_name = "%s.%s" % (name, ext)
    return os.path.join('employees', full_name)


# Create your models here.
class Employee(models.Model):
    #name, email, dob, salary, disabled
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    dob = models.DateField(null=True)
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    disabled = models.BooleanField(default=False)
    profile = models.ImageField(upload_to=unique_img_name, null=True, default="employees/employee.png")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return self.name
    
# module package library