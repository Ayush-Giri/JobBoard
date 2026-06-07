from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()
class Skills(models.Model):
    name = models.CharField(max_length=200, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} | {self.user.username}"
    
    

    

