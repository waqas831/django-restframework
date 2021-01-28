from django.db import models

# Create your models here.
class Detail(models.Model):
    name=models.CharField(max_length=30)
    fname=models.CharField(max_length=40)
    age=models.IntegerField()
    address=models.CharField(max_length=40)
    city=models.CharField(max_length=40)

    def __str__(self):
        return self.name+' '+self.address
