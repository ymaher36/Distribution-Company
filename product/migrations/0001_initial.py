# Generated by Django 4.1.4 on 2022-12-26 19:08

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70, verbose_name='الماركة')),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70, verbose_name='النوع')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70, verbose_name='اسم المنتج')),
                ('image', models.CharField(blank=True, max_length=70, verbose_name='صورة المنتج')),
                ('product_brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.brand', verbose_name='ماركة المنتج')),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.producttype', verbose_name='نوع المنتج')),
            ],
        ),
    ]