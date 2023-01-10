import uuid

from django.db import models


# Create your models here.
class City(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)


class Location(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    street = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
