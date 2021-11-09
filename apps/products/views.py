from django.shortcuts import render
from django.views import generic
from apps import products
from apps.products.models import Product, Like

# Create your views here.
def detail_product(request, slug):
    products = Product.objects.get(slug = slug)
    if 'like' in request.POST:
        try:
            like = Like.objects.get(user=request.user, products=products)
            like.delete()
        except:
            Like.objects.create(user=request.user, products=products)

    return render(request, 'products/detail.html', {'product' : products})