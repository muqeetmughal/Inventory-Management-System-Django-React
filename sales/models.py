from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
from django.utils.translation import gettext_lazy as _
import datetime

User = get_user_model()


class Customer(models.Model):
    name = models.CharField(max_length=125, null=False,
                            blank=False, default=None)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=14, null=True, blank=True)
    opening_balance = models.FloatField(null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    postal_code = models.CharField(max_length=10, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    # def save(self, *args, **kwargs):
    #     if not self.id:
    #     # Object is a new instance

    #     return super(Customer, self).save(*args, **kwargs)


class SaleItem(models.Model):
    product = models.ForeignKey(
        'inventory.Product', on_delete=models.CASCADE, null=False, blank=False, default=None)
    quantity = models.IntegerField()


class Sale(models.Model):

    date = models.DateField(default=datetime.date.today)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField("SaleItem")
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

    class PAYMENT_CHOICES(models.TextChoices):
        CASH = 'cash', _('Cash')
        BANKTRANSFER = 'banktransfer', _('Bank Transfer')
        CHEQUE = 'cheque', _('Cheque')
        UNPAID = 'unpaid', _('Unpaid')

    payment_method = models.CharField(
        max_length=20, choices=PAYMENT_CHOICES.choices, default=PAYMENT_CHOICES.UNPAID)

    type = models.CharField(
        max_length=20, choices=TYPE_CHOICES.choices, default=TYPE_CHOICES.NEW)
