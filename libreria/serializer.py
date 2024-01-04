from rest_framework import serializers
from .models import Users, Book

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'name', 'email']
        

class BookSerializer(serializers.ModelSerializer):
    users = UserSerializer(many = True, read_only = True)

    class Meta: 
        model = Book
        fields = ('id', 'title', 'autor', 'isbn', 'release_date', 'users_id', 'users')

   