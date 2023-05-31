import uuid

from django.db import models

from inventory.branches.models import Branch
from locations.addresses.models import Location


class PhoneNumber(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.CharField(max_length=11)


class CustomerType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)


class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    branch = models.ManyToManyField(Branch)
    location = models.ManyToManyField(Location)
    type = models.ForeignKey(CustomerType, on_delete=models.CASCADE)
    phone_number = models.ManyToManyField(PhoneNumber)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
