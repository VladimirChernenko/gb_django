from multiprocessing import context
from django.shortcuts import render
import json
from .models import Category, Product

# Create your views here.
def main(request):
    context = {'category': Category.objects.all(), 'product': Product.objects.all()}
    return render(request, 'mainapp/index.html', context)

def products(request):
    context = {'category': Category.objects.all(), 'product': Product.objects.all()}
    return render(request, 'mainapp/products.html', context)

def products_category(requests, pk=None):
    context = {'category': Category.objects.all(), 'product': Product.objects.all()}
    return render(requests, 'mainapp/products.html', context)

def contact(request):
    return render(request, 'mainapp/contact.html')
