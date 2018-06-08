from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView
from product_manager.models import Category, Product
from core_site.models import Market, TheBestProduct
from core_site.forms import ProductForm

class IndexListView(ListView):
    model = Product
    form = ProductForm
    template_name = 'core_site/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'recommend_products': TheBestProduct.objects.all(),
            'basic_settings': Market.objects.all()[0],
        })
        return context

class ContactTemplateView(TemplateView):
    template_name = 'core_site/contact.html'

    def get(self, request):
        form = ProductForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            form = ProductForm
            return redirect('contact')
        args = {'form': form, 'basic_settings': Market.objects.all()[0]}
        return render(request, self.template_name, args)

class NewsListView(ListView):
    template_name = 'core_site/news.html'

    def get_queryset(self):
      pass

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'basic_settings': Market.objects.all()[0],
        })
        return context