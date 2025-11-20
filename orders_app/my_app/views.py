from django.shortcuts import render
from django.http import HttpResponse
from my_app.models import Product
# Create your views here.



def home(request):

    return HttpResponse([{"name": prod.name, "desc":prod.description, "price":prod.price} for prod in Product.objects.all()])
