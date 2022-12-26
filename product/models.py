from django.db import models
import uuid


# Create your models here.


class ProductType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=70, null=False,
                            blank=False, verbose_name="النوع")


class Brand(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=70, null=False,
                            blank=False, verbose_name="الماركة")


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=70, null=False,
                            blank=False, verbose_name="اسم المنتج")
    image = models.CharField(max_length=70, blank=True,
                             verbose_name='صورة المنتج')
    product_type = models.ForeignKey(
        ProductType, on_delete=models.PROTECT, null=False, verbose_name="نوع المنتج")
    product_brand = models.ForeignKey(
        Brand, on_delete=models.PROTECT, null=False, verbose_name="ماركة المنتج")
