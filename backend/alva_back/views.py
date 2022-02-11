from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend

class ProductCreate(generics.CreateAPIView):
    serializer_class = ProductSerializer

class ProductListAll(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class ProductListCats(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        cat = self.request.query_params.get('cat')
        if cat is not None:
            queryset = queryset.filter(category=cat)
        return queryset

class ProductListSale(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        queryset = queryset.filter(sale=True)
        return queryset

class ProductListNew(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        queryset = queryset.filter(new_col=True)
        return queryset

class GetProduct(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductListDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class OrderListAll(generics.ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class OrderCreate(generics.CreateAPIView):
    serializer_class = OrderSerializer

class OrderListDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
