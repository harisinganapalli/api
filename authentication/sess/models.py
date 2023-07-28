from django.db import models

# Create your models here.
class Employee (models.Model):
    name=models.CharField(max_length=100)
    empid=models.CharField(max_length=15)
    phonenumber=models.CharField(max_length=10)
    city=models.CharField(max_length=100)
    email=models.CharField(max_length=100)



    def __str__(self):
        return self.name
    
    
