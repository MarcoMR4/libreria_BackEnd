from rest_framework import serializers
from .models import Users, Book

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
        

class BookSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Book
        fields = '__all__'