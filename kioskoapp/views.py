from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters

from .models import Product
from .serializers import ProductSerializer
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
    filter_backends = [filters.SearchFilter]
    filterset_fields = ['codigo']