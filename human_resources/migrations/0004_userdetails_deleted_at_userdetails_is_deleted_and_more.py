# Generated by Django 4.1 on 2023-06-07 10:22

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
        ('human_resources', '0003_alter_phonenumber_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='phonenumber',
            name='phone_number',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='home_location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='locations.location'),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='national_id',
            field=models.CharField(max_length=14, null=True, unique=True, validators=[django.core.validators.MinLengthValidator(14)]),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='human_resources.role'),
        ),
    ]
