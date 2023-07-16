from rest_framework import serializers
from .models import Product
class ProductsSerializer(serializers.ModelSerializer):
    """Product serializer."""
    class Meta:
        model = Product
        fields = '__all__'