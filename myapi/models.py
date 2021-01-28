from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30)
    fname=models.CharField(max_length=30)
    roll=models.IntegerField(default=0)
    semester=models.IntegerField(default=0,blank=False)
    city=models.CharField(max_length=40)


    def __str__(self):
        return self.name+' '+self.fname
