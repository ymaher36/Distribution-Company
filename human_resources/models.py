from django.db import models
import uuid


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
    role = models.ForeignKey(Role, on_delete=models.PROTECT, null=True)
    # home_location =
