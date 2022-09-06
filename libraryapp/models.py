from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100,unique=True)
    Author = models.CharField(max_length=50)
    status = models.BooleanField()

    def __str__(self):
        return self.name

