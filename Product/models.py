from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    weight = models.FloatField(default=0.0)
    price = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)