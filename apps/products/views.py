from django.shortcuts import render
from django.views import generic
from apps.products.models import Product

# Create your views here.
class ProductIndexView(generic.ListView):
    model = Product
    template_name = 'products/detail.html'
    context_object_name = 'product'
