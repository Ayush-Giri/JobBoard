from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Skills(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f"{self.name} | {self.user.username}"
    
    

    

