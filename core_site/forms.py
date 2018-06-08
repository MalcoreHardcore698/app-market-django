from django import forms
from product_manager.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'extra_information', 'category', 'price', 'currency']

