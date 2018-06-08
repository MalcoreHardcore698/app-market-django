from django.db import models
from product_manager.models import Category, Product

class Market(models.Model):
    name_market = models.CharField(max_length=64, default='Django Market',
                                   blank=True,
                                   null=True)
    desc_market = models.TextField(default='Welcome to my Market! Here you finded a lot of product special for us.',
                                   blank=True,
                                   null=True)
    keywords = models.TextField(blank=True,
                                null=True)

    def __str__(self):
        return self.name_market

class TheBestProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name