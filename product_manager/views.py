from django.shortcuts import render
from django.views.generic import ListView, DetailView
from product_manager.models import Category, Product, Attribute

class IndexListView(ListView):
    model = Product
    template_name = 'product_manager/catalog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_product'] = Product.objects.all()
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_manager/product.html'
