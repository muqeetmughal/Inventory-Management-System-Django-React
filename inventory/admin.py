from django.contrib import admin

from inventory.models import Brand, Category, Product, ProductImage, Warehouse

# Register your models here.
admin.site.register([Warehouse, Brand, Category, ProductImage, Product])
