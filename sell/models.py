from django.db import models

# Create your models here.

class Sell(models.Model):
    username = models.CharField(max_length=20)
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    contact = models.CharField(max_length=10)
    description = models.CharField(max_length=100)