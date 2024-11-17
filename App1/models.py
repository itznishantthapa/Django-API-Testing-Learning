from django.db import models

# Create your models here.
class FoodItem(models.Model):
    name=models.CharField(max_length=50,blank=True,null=True)
    price=models.IntegerField(blank=True,null=True)
    description=models.TextField(max_length=100,blank=True,null=True)

class FoodWithImage(models.Model):
    image=models.ImageField(upload_to='images/')
    name=models.CharField(max_length=50,blank=True,null=True)