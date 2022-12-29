from django.db import models
import uuid


# Create your models here.


class ProductType(models.Model):
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
    expire_at = models.DateField(null=True)

    def product_full_name(self):
        return self.product_type.name + ' -- ' + self.product_brand.name + ' -- ' + self.name

    def __str__(self):
        return self.product_full_name()


class Branch(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    products = models.ManyToManyField(Product)


class BranchPhoneNumber(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_number = models.IntegerField()
    branch = models.ForeignKey(Branch, on_delete=models.PROTECT)
