from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class JobTypeChoices(models.TextChoices):
    PART_TIME = ("part_time", "part_time")
    REMOTE = ("remote", "remote")
    FULL_TIME = ("full_time", "full_time")
    CONTRACT = ("contract", "contract")

class JobPosting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    company_name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    job_type = models.CharField(max_length=50, choices=JobTypeChoices.choices)
    salary = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.title} | {self.company_name}"


