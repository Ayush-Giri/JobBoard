from django.db import models
from django.contrib.auth import get_user_model
from helpers import generate_random_string

# Create your models here.

User = get_user_model()

class EmailVerificationLink(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    unique_link = models.CharField(max_length=200, unique=True, default=generate_random_string)
    is_used = models.BooleanField(default=False)


    def save(self, *args, **kwargs):
        if self.is_used:
            self.user.is_email_verified = True
            self.user.save()
        super().save(*args, **kwargs)

