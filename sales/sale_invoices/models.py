import uuid

from django.contrib.auth import get_user_model
from django.db import models

from inventory.branches.models import Branch
from purchases.purchase_invoices.models import PurchaseProduct
from sales.customers.models import Customer


class SellingChannel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True)
    selling_channel = models.ForeignKey(SellingChannel, on_delete=models.CASCADE, null=True)
    total_price = models.FloatField(null=True)
    discount = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    receiving_date = models.DateField(null=True)
    amount_of_boxes = models.FloatField(null=True)
    amount_of_types = models.IntegerField(null=True)
    amount_of_brands = models.IntegerField(null=True)
    note = models.CharField(max_length=400, null=True)
    state = models.CharField(max_length=20, null=False, blank=False, default='pending')
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="create_user")
    delivered_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, related_name="deliver_user")


class OrderProducts(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(PurchaseProduct, on_delete=models.CASCADE, null=True)
    quantity = models.FloatField()
    price = models.FloatField(null=True)


class PricingList(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    selling_price = models.FloatField()
    end_date = models.DateTimeField(null=True)
    product = models.ForeignKey(PurchaseProduct, on_delete=models.CASCADE, related_name="pricing_list")
