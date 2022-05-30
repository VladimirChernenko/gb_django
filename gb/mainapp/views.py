from multiprocessing import context
from django.shortcuts import render
import json
from .models import Category, Product


# Create your views here.
def main(request):
    return render(request, 'mainapp/index.html')

def products(request):
    categ = Category.objects.name()
    links_menu = [{'href': 'products', 'title': el} for el in categ]
    return render(request, 'mainapp/products.html', context={'links_menu': links_menu,})

def contact(request):
    return render(request, 'mainapp/contact.html')
