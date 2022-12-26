from django.db import models
import uuid

from product.models import Product


# Create your models here.
class Branch(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    captial = models.FloatField()
    products = models.ManyToManyField(Product)


class BranchPhoneNumbers(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_number = models.IntegerField()
    branch = models.ForeignKey(Branch, on_delete=models.PROTECT)
