import uuid
from django.contrib.auth import get_user_model

from django.db import models
from django.utils import timezone

from inventory.branches.models import Branch
from purchases.purchase_invoices.models import Purchase
from sales.sale_invoices.models import Order


class ExpenseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class ExpenseType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40, null=True)


class Expense(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    branch = models.ForeignKey(Branch, on_delete=models.PROTECT)
    type = models.ForeignKey(ExpenseType, on_delete=models.PROTECT, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    purchase = models.ForeignKey(Purchase, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    note = models.TextField(blank=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = models.Manager()
    active = ExpenseManager()

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
