from django.db import models

# Create your models here.
class User(models.Model):
    user_name=models.CharField(max_length=30, unique=True)
    user_email=models.CharField(max_length=30,unique=True)
    password=models.CharField()

