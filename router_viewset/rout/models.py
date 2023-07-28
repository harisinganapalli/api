from django.db import models

# Create your models here.
class Book (models.Model):
    author=models.CharField(max_length=120)
    bookname=models.CharField(max_length=150)
    published_year=models.CharField(max_length=4)
    typeofbook=models.CharField(max_length=120)


    def __str__(self):
        return self.bookname