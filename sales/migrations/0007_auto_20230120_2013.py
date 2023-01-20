# Generated by Django 3.2.16 on 2023-01-20 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('human_resources', '0007_alter_user_home_location_alter_user_role'),
        ('sales', '0006_auto_20230120_2008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='create_user',
        ),
        migrations.AddField(
            model_name='order',
            name='created_by',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='create_user', to='human_resources.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='delivered_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='deliver_user', to='human_resources.user'),
        ),
    ]
