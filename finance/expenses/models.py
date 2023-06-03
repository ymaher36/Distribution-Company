import uuid
from django.contrib.auth import get_user_model

from django.db import models

from inventory.branches.models import Branch
from purchases.purchase_invoices.models import Purchase
from sales.sale_invoices.models import Order


class ExpenseType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40, null=True)


class Expense(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.FloatField(null=True)
    branch = models.ForeignKey(Branch, on_delete=models.PROTECT)
    type = models.ForeignKey(ExpenseType, on_delete=models.PROTECT, null=True)
    order = models.ForeignKey(Order, on_delete=models.PROTECT, null=True)
    purchase = models.ForeignKey(Purchase, on_delete=models.PROTECT, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    note = models.CharField(max_length=500, null=True)
