# Generated by Django 4.1 on 2023-05-01 18:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('national_id', models.CharField(max_length=14, null=True, unique=True)),
                ('start_work_date', models.DateField(null=True)),
                ('end_work_date', models.DateField(null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('birthdate', models.DateField(null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('branch', models.ManyToManyField(to='inventory.branch')),
                ('home_location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.location')),
                ('role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='human_resources.role')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('phone_number', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
