import uuid

from django.db import models

from inventory.branches.models import Branch
from locations.addresses.models import Location


class SupplierType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)


class Supplier(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    location = models.ManyToManyField(Location)
    type = models.ForeignKey(SupplierType, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

