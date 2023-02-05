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
    name = models.CharField(max_length=50, null=True, unique=True)
    start_work_date = models.DateField(null=True)
    end_work_date = models.DateField(null=True)
    national_id = models.CharField(null=True, max_length=14, unique=True)
    gender = models.CharField(max_length=10, null=True)
    birthdate = models.DateField(null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    home_location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    phone_numbers = models.ForeignKey(PhoneNumber, on_delete=models.CASCADE, null=True)
    created_at = models.DateField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.role.name + '---' + self.name
