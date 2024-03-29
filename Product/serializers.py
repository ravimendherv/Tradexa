from rest_framework import fields, serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name','weight','price','created_at','updated_at']