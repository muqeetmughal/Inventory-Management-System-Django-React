from email.policy import default
from django.db import models

from django.utils.translation import gettext_lazy as _
# Create your models here.

class Warehouse(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

class Product(models.Model):

    name = models.CharField(max_length=255, null=False, blank=False)
    brand = models.ForeignKey(
        "Brand", on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(
        "Category", on_delete=models.SET_NULL, null=True, blank=True)

    sku = models.CharField(max_length=20, null=True, blank=True)
    hsn = models.CharField(max_length=6, null=True, blank=True)
    minimum_quantity = models.IntegerField(default=0)
    lot_number = models.CharField(max_length=50, null=True, blank=True)
    expiry_date = models.DateField()
    desciption = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="products")
    price = models.FloatField()
    profit_margin = models.FloatField()

    class BARCODE_SYMBOLOGY_CHOICES(models.TextChoices):
        CODE128 = 'code128', _('Code 128')
        CODE39 = 'code39', _('Code 39')

    barcode_symbology = models.CharField(
        max_length=20, choices=BARCODE_SYMBOLOGY_CHOICES.choices, default=BARCODE_SYMBOLOGY_CHOICES.CODE128)


class ProductImage(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products/images")

    def __str__(self) -> str:
        return self.product.name


class Brand(models.Model):
    name = models.CharField(max_length=125, null=False, blank=False)
    logo = models.ImageField(upload_to="brands", default=None)

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=125, null=False, blank=False)

    def __str__(self) -> str:
        return self.name
