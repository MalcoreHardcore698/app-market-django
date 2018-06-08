from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.IndexListView.as_view(), name='index'),
    url(r'^news/$', views.NewsListView.as_view(), name='news'),
    url(r'^contact/$', views.ContactTemplateView.as_view(), name='contact'),
]
