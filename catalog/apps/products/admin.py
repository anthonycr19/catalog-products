from django.contrib import admin
from .models import Product, LogUserReadProduct


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'name', 'price')


@admin.register(LogUserReadProduct)
class LogUserReadProductAdmin(admin.ModelAdmin):
    pass
