from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.IndexListView.as_view(), name='catalog'),
    url(r'^product/(?P<pk>[\w-]+)/$', views.ProductDetailView.as_view(), name='product')
]