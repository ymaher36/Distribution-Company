import uuid

from django.db import models


# Create your models here.
class Governorate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)


class District(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    governorate = models.ForeignKey(Governorate, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)


class Location(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    street = models.CharField(max_length=50)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    other = models.CharField(max_length=300)
    # lat_lng
