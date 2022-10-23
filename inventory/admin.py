from django.contrib import admin

from inventory.models import Brand, Category, Product, ProductImage

# Register your models here.
admin.site.register([Brand, Category, ProductImage, Product])
