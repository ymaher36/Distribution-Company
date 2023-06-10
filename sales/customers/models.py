import uuid

from django.db import models
from django.utils import timezone

from inventory.branches.models import Branch
from locations.addresses.models import Location


class PhoneNumber(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.CharField(max_length=11)


class CustomerType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)


class CustomerManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    branch = models.ManyToManyField(Branch)
    location = models.ManyToManyField(Location)
    type = models.ForeignKey(CustomerType, on_delete=models.CASCADE)
    phone_number = models.ManyToManyField(PhoneNumber)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = models.Manager()
    active = CustomerManager()

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
