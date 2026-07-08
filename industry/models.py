from django.db import models

# Create your models here.

class Industry(models.Model):
    name = models.CharField()

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"
