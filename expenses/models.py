import datetime
from django.db import models

# Create your models here.


class ExpenseCategory(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)

    def __str__(self) -> str:
        return self.name


class Expense(models.Model):
    date = models.DateField(default=datetime.date.today)
    title = models.CharField(max_length=128, null=False, blank=False)
    category = models.ForeignKey("ExpenseCategory", on_delete=models.CASCADE)
    amount = models.FloatField(null=False, blank=False)
    detail = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title
