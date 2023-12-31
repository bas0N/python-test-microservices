from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from .models import Product, User
from .serializers import ProductsSerializer
from rest_framework.views import APIView
from .producer import publish
import random
# Create your views here.

class ProductViewSet(viewsets.ViewSet):
    """Product view set."""
    def list(self,request): # /api/products
        """List all products."""
        publish()
        products = Product.objects.all()
        serializer = ProductsSerializer(products,many=True)
        return Response(serializer.data)

    def create(self,request): # /api/products
        """Create new product."""
        serializer = ProductsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('product_created',serializer.data)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    def retrieve(self,request,pk=None): # /api/products/<str:id>
        """Get product by id."""
        product = Product.objects.get(id=pk)
        serializer = ProductsSerializer(product)
        return Response(serializer.data)

    def update(self,request,pk=None): # /api/products/<str:id>
        """Get product by id."""
        product = Product.objects.get(id=pk)
        serializer = ProductsSerializer(instance=product,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('product_updated',serializer.data)
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)


    def destroy(self,request,pk=None): # /api/products/<str:id>
        """Get product by id."""
        product = Product.objects.get(id=pk)
        product.delete()
        publish('product_deleted',pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserAPIView(APIView):
    """User API view."""
    def get(self,request):
        """Get user."""
        users = User.objects.all()
        user = random.choice(users)
        return Response({
            'id': user.id
        })