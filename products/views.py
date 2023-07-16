from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.

class ProductViewSet(viewsets.ViewSet):
    """Product view set."""
    def list(self,request): # /api/products
        """List all products."""
        pass

    def create(self,request): # /api/products
        """Create new product."""
        pass

    def retrieve(self,request,pk=None): # /api/products/<str:id>
        """Get product by id."""

    def update(self,request,pk=None): # /api/products/<str:id>
        """Get product by id."""

    def delete(self,request,pk=None): # /api/products/<str:id>
        """Get product by id."""