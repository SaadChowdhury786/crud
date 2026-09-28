from django.db import models

class Employee(models.Model):
    name= models.CharField(max_length=90)
    roll = models.IntegerField()



    def __str__(self):
       return self.name
