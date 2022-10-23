from django.contrib import admin
from purchases.models import Purchase, PurchaseItem, Supplier
# Register your models here.
admin.site.register([Supplier, Purchase, PurchaseItem])
