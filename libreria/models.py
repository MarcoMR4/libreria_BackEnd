from django.db import models
from django.contrib.auth.hashers import make_password



class Users(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    
    def save(self, *args, **kwargs):
        if not self.password.startswith(('pbkdf2_sha256$', 'bcrypt')):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)


class Book(models.Model): 
    title = models.CharField(max_length=500, default='Sin título')
    autor = models.CharField(max_length=255)
    isbn = models.CharField(max_length=255)
    release_date = models.DateField()
    users_id = models.ForeignKey(Users, on_delete=models.CASCADE)
