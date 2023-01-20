import uuid

from django.db import models

from human_resources.models import User
from inventory.products.models import Branch, Product, PricingList
from locations.models import Location
from purchases.models import PurchaseProduct


# Create your models here.


class SellingChannel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=50)


class CustomerType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=20)


class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    location = models.ManyToManyField(Location)
    type = models.ForeignKey(CustomerType, on_delete=models.CASCADE)


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True)
    selling_channel = models.ForeignKey(SellingChannel, on_delete=models.CASCADE, null=True)
    total_price = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    receiving_date = models.DateField(null=True)
    amount_of_boxes = models.FloatField(null=True)
    amount_of_types = models.IntegerField(null=True)
    amount_of_brands = models.IntegerField(null=True)
    note = models.CharField(max_length=400, null=True)
    state = models.CharField(max_length=20, null=False, blank=False, default='pending')

    create_user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_user = models.ForeignKey(User, on_delete=models.CASCADE)


class OrderProducts(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(PurchaseProduct, on_delete=models.CASCADE, null=True)
    quantity = models.FloatField()
