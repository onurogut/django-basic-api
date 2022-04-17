from django.db import models

# Create your models here.

class Book(models.Model):
    bookname = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    page = models.IntegerField()
    type = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)