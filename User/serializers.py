from django.db import models
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        User.username = models.CharField(max_length=30,primary_key=True)
        User.email =  models.EmailField(unique=True)
        fields = ['email','first_name', 'last_name', 'username', 'password']
        extra_kwargs = {'email':{'write_only':True}, 'password':{'write_only':True},'first_name':{'write_only':True},'last_name':{'write_only':True}}
        def create(self, validate_data):
            user = User.objects.create_user(**validate_data)
            return user

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['user','text', 'created_at', 'updated_at']
        
