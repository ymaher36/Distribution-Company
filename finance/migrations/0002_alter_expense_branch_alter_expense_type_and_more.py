# Generated by Django 4.1 on 2023-01-10 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_alter_branch_location_alter_branchphonenumber_branch_and_more'),
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.branch'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.expensetype'),
        ),
        migrations.AlterField(
            model_name='income',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.branch'),
        ),
        migrations.AlterField(
            model_name='income',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.incometype'),
        ),
    ]
