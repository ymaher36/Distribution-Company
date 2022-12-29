# Generated by Django 4.1 on 2022-12-29 14:08

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_product_expire_at'),
        ('sales', '0002_sellingchannel_order_branch_order_create_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PricingList',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('purchasing_price', models.FloatField()),
                ('selling_price', models.FloatField()),
                ('end_date', models.DateTimeField(null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.product')),
            ],
        ),
    ]
