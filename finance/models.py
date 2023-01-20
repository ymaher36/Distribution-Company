import uuid

from django.db import models

from inventory.products.models import Branch


# Create your models here.

class ExpenseType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40, null=True)


class Expense(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.FloatField(null=True)
    note = models.CharField(max_length=500, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    type = models.ForeignKey(ExpenseType, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)


class IncomeType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40, null=True)


class Income(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.FloatField(null=True)
    note = models.CharField(max_length=500, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    type = models.ForeignKey(IncomeType, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
