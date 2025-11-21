from django.shortcuts import render
from django.http import HttpResponse
from my_app.models import Product, Order, User
from .serializers import ProductSerializer, OrderSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Create your views here.



class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        return queryset.exclude(name=None)

class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(user=User.objects.last())