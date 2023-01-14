import datetime

from django.db import models
import uuid

from locations.models import Location


# Create your models here.


class ProductCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=70, null=False,
                            blank=False, verbose_name="النوع")

    def __str__(self):
        return self.name


class Brand(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=70, null=False,
                            blank=False, verbose_name="الماركة")

    def __str__(self):
        return self.name


class PricingList(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    purchasing_price = models.FloatField()
    selling_price = models.FloatField()
    end_date = models.DateTimeField(null=True)


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=70, null=False,
                            blank=False, verbose_name="اسم المنتج")
    image = models.CharField(max_length=70, blank=True,
                             verbose_name='صورة المنتج')
    product_category = models.ForeignKey(
        ProductCategory, on_delete=models.CASCADE, null=False, verbose_name="نوع المنتج")
    product_brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, null=False, verbose_name="ماركة المنتج")
    expire_at = models.DateField(null=True)
    price_list = models.ManyToManyField(PricingList)
    created_at = models.DateField(auto_now_add=True, blank=True)

    def product_full_name(self):
        return self.product_category.name + ' -- ' + self.product_brand.name + ' -- ' + self.name

    def __str__(self):
        return self.product_full_name()


class Branch(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)


class ProductBranch(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.FloatField()


class BranchPhoneNumber(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_number = models.CharField(max_length=20)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
