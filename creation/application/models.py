from django.db import models

# Create your models here.
class Fruits(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=600) 


    def __str__(self):
        return self.name