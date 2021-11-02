from django.shortcuts import render
from django.views import generic
from apps.categories.models import Category


# Create your views here.
class CategoryIndexView(generic.ListView):
    model = Category
    template_name = 'categories/index.html'
    context_object_name = 'categories'
