# Generated by Django 4.1 on 2022-12-29 14:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('human_resources', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.RenameModel(
            old_name='phone_numbers',
            new_name='PhoneNumber',
        ),
    ]