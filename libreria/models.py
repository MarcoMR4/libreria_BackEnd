from django.db import models

# Create your models here.

class Users(models.Model):
    email = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)



class Book(models.Model): 
    title = models.CharField(max_length=500, default='Sin título')
    autor = models.CharField(max_length=255)
    isbn = models.CharField(max_length=255)
    release_date = models.DateField()
    users_id = models.ForeignKey(Users, on_delete=models.CASCADE)
