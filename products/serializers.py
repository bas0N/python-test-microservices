from rest_framework import serializers
from .models import Products
class ProductsSerializer(serializers.ModelSerializer):
    """Product serializer."""
    class Meta:
        model = Products
        fields = '__all__'