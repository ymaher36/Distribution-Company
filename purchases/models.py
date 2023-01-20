import uuid

from django.db import models

from inventory.branches.models import Branch
from inventory.products.models import Product
from locations.models import Location


# Create your models here.
class PurchasingChannel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=50)


class SellerType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=20)


class Seller(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    location = models.ManyToManyField(Location)
    type = models.ForeignKey(SellerType, on_delete=models.CASCADE)


class Purchase(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    total_price = models.FloatField(null=True)
    amount_of_boxes = models.FloatField(null=True)
    amount_of_types = models.IntegerField(null=True)
    amount_of_brands = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    receiving_date = models.DateField(null=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    type = models.CharField(max_length=20)
    purchase_channel = models.ForeignKey(PurchasingChannel, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    note = models.CharField(max_length=400)


class PurchaseProduct(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    price = models.FloatField(null=True)
    expire_date = models.DateField(null=True)
    quantity = models.IntegerField(null=True)
