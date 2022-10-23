from django.db import models
import datetime
# Create your models here.

from django.utils.translation import gettext_lazy as _


class Supplier(models.Model):
    name = models.CharField(max_length=125, null=False,
                            blank=False, default=None)
    email = models.EmailField(null=False, blank=False)
    phone = models.CharField(max_length=14, null=False, blank=False)
    country = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    postal_code = models.CharField(max_length=10, null=True, blank=True)
    address = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self) -> str:
        return self.name


class PurchaseItem(models.Model):
    product = models.ForeignKey(
        'inventory.Product', on_delete=models.CASCADE, null=False, blank=False, default=None)
    quantity = models.IntegerField()


class Purchase(models.Model):
    date = models.DateField(default=datetime.date.today)
    supplier = models.ForeignKey("Supplier", on_delete=models.CASCADE)
    products = models.ManyToManyField("PurchaseItem")
    order_tax = models.FloatField(default=0)
    discount = models.FloatField(default=0)
    shipping = models.FloatField(default=0)

    class STATUS_CHOICES(models.TextChoices):
        RECIEVED = 'recieved', _('Recieved')
        ORDERED = 'ordered', _('Ordered')
        PENDING = 'pending', _('Pending')

    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES.choices, default=STATUS_CHOICES.RECIEVED)

    notes = models.TextField(null=True, blank=True)

    class TYPE_CHOICES(models.TextChoices):
        NEW = 'new', _('New')
        RETURN = 'return', _('Return')

    type = models.CharField(
        max_length=20, choices=TYPE_CHOICES.choices, default=TYPE_CHOICES.NEW)
