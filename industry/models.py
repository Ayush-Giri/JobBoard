from django.db import models

# Create your models here.

class Industry(models.Model):
    name = models.CharField()

    def save(self, *args, **kwarsg):
        self.name = self.name.title()

    def __str__(self):
        return f"{self.name}"
