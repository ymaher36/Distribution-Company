# Generated by Django 4.1 on 2022-12-28 15:56

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SellingChannel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='inventory.branch'),
        ),
        migrations.AddField(
            model_name='order',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='sales.customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='number_of_boxes',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='number_of_types',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='receiving_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='state',
            field=models.CharField(default='pending', max_length=20),
        ),
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.FloatField(null=True),
        ),
        migrations.CreateModel(
            name='OrderProducts',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('quantity', models.FloatField()),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='sales.order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='inventory.product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='selling_channel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='sales.sellingchannel'),
        ),
    ]
