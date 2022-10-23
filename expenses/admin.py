from django.contrib import admin

from expenses.models import Expense, ExpenseCategory

# Register your models here.


admin.site.register([Expense, ExpenseCategory])