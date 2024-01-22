from django.shortcuts import render
from django.views import generic
from .models import Product


class ProductListView(generic.ListView):
    model = Product
    queryset = Product.objects.filter(active=True)
    context_object_name = 'products'

class ProductDetailView(generic.DetailView):
    model = Product