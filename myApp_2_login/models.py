from django.db import models

# Create your models here.

#The class name represents the database table name
class User(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)