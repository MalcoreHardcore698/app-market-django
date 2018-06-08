from django.db import models
from django.urls import reverse, resolve

class GroupCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Category(models.Model):
    group = models.ForeignKey(GroupCategory,
                              blank=True,
                              null=True,
                              on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class GroupAttribute(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Attribute(models.Model):
    group = models.ForeignKey(GroupAttribute,
                              blank=True,
                              null=True,
                              on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    value = models.TextField(blank=True,
                             null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    extra_information = models.CharField(max_length=64,
                                         blank=True,
                                         null=True)
    category = models.ForeignKey(Category,
                                 blank=True,
                                 null=True,
                                 on_delete=models.CASCADE)

    USD = '$'
    EUR = '€'
    RUB = '₽'
    CURRENCYS = (
        (USD, 'USD'),
        (EUR, 'EUR'),
        (RUB, 'RUB'),
    )
    price = models.FloatField(default=0.0)
    currency = models.CharField(verbose_name='', max_length=3,
                                choices=CURRENCYS,
                                default=USD)

    attributes = models.ManyToManyField(Attribute, blank=True)
    img = models.ImageField(default='/default.png',
                            blank=True,
                            null=True)

    def get_absolute_url(self):
        #return resolve("/catalog/product/" + str(self.name))
        return reverse('product', args=[self.id])

    def __str__(self):
        return self.name
