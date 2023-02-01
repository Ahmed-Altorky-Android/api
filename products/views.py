from django.shortcuts import render
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializers
# Create your views here.

class ProductDetailAPIView(generics.RetrieveAPIView):
   queryset = Product.objects.all()
   serializer_class = ProductSerializers
   # lookup_field = 'pk'
product_detail_view = ProductDetailAPIView.as_view()
