from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    eid = models.CharField(max_length=50)
    salary = models.IntegerField()
    position = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.name
    
    