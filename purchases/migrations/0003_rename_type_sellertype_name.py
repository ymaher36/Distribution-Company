# Generated by Django 4.1 on 2023-03-23 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0002_seller_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sellertype',
            old_name='type',
            new_name='name',
        ),
    ]
