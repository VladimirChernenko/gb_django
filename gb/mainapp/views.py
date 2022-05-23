from multiprocessing import context
from django.shortcuts import render
import json

# Create your views here.
def main(request):
    return render(request, 'mainapp/index.html')

def products(request):
    with open('file.json', 'w') as f:
        json.dump([
        {'href': 'products_all', 'title': 'все'},
        {'href': 'products_home', 'title': 'дом'},
        {'href': 'products_office', 'title': 'офис'},
        {'href': 'products_modern', 'title': 'модерн'},
        {'href': 'products_classic', 'title': 'классика'},
    ], f)
    with open('file.json') as f:
        links_menu = json.loads(f.read())
    context = {'links_menu': links_menu}
    return render(request, 'mainapp/products.html', context)

def contact(request):
    return render(request, 'mainapp/contact.html')
