from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name