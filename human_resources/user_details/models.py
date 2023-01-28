from django.db import models
import uuid

from locations.addresses.models import Location


# Create your models here.
class PhoneNumber(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_number = models.CharField(max_length=20)


class Role(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30, null=True)


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, null=True)
    start_work_date = models.DateTimeField(null=True)
    end_work_date = models.DateTimeField(null=True)
    national_id = models.IntegerField(null=True)
    birthdate = models.DateField(null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    home_location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    phone_numbers = models.ForeignKey(PhoneNumber, on_delete=models.CASCADE, null=True)
