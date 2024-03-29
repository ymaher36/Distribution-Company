import datetime

from django.db import models
import uuid

from django.utils import timezone


# Create your models here.


class ProductCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=70, null=False,
                            blank=False, verbose_name="النوع", unique=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=70, null=False,
                            blank=False, verbose_name="الماركة", unique=True)

    def __str__(self):
        return self.name


class ProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=70, null=False,
                            blank=False, verbose_name="اسم المنتج")
    image = models.CharField(max_length=70, blank=True,
                             verbose_name='صورة المنتج')
    category = models.ForeignKey(
        ProductCategory, on_delete=models.CASCADE, null=False, verbose_name="نوع المنتج")
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, null=False, verbose_name="ماركة المنتج")
    created_at = models.DateField(auto_now_add=True, blank=True)

    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = models.Manager()
    active = ProductManager()

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def product_full_name(self):
        return self.category.name + ' -- ' + self.brand.name + ' -- ' + self.name

    def __str__(self):
        return self.product_full_name()
