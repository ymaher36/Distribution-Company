# Generated by Django 4.1 on 2023-01-25 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('human_resources', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_numbers',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='human_resources.phonenumber'),
        ),
    ]
