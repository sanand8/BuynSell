from django.db import models

class SignUp(models.Model):
    username=models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    contact = models.IntegerField()
    email = models.EmailField(max_length=254)
    hostel = models.CharField(max_length=20)
    room = models.IntegerField()
    pwd = models.CharField(max_length=100)