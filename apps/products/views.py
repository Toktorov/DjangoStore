from django.shortcuts import render
from django.views import generic
from apps import products
from apps.products.models import Product

# Create your views here.
def detail_product(request, slug):
    product = Product.objects.get(slug = slug)
    return render(request, 'products/detail.html', {'product' : product})