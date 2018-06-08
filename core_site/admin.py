from django.contrib import admin
from product_manager.models import Category, GroupCategory, Product, Attribute, GroupAttribute
from core_site.models import Market, TheBestProduct

class AdminCategory(admin.ModelAdmin):
    pass

class AdminGroupCategory(admin.ModelAdmin):
    pass

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'category', 'id']
    fieldsets = (
        (None, {
            'fields': ('name', 'extra_information', 'category', ('price', 'currency'))
        }),
        ('Advanced options', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('img', 'attributes'),
        }),
    )

class AdminAttribute(admin.ModelAdmin):
    pass

class AdminGroupAttribute(admin.ModelAdmin):
    pass

class AdminTheBestProduct(admin.ModelAdmin):
    pass

admin.site.register(Market)
admin.site.register(Category, AdminCategory)

admin.site.register(GroupCategory, AdminGroupCategory)
admin.site.register(Attribute, AdminAttribute)

admin.site.register(GroupAttribute, AdminGroupAttribute)
admin.site.register(Product, AdminProduct)

admin.site.register(TheBestProduct, AdminTheBestProduct)