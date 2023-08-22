from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    name  = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre, blank=True)
    description = models.TextField()
    quantity = models.IntegerField()
    
    def __str__(self):
        return self.name
