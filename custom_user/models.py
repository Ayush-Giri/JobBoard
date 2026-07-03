from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Role(models.TextChoices):
    EMPLOYER = ("employer", "Employer")
    APPLICANT = ("applicant", "Applicant")

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20)
    role = models.CharField(choices=Role.choices)
    is_email_verified = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.username} | {self.role} | {self.phone_number}"
    

