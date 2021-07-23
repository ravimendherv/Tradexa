from django.contrib import admin
from django.contrib.auth.models import User
from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user','text', 'created_at', 'updated_at']
