from django.db import models


# Create your models here.

class User(models.Model):
    user_Id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=1000)
    Discription = models.CharField(max_length=5000,default=' ')

    def __str__(self):
        return self.Title


class Author(models.Model):
    Author_Id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=1000)
    Discription = models.CharField(max_length=5000,default=' ')

    def __str__(self):
        return self.Title



