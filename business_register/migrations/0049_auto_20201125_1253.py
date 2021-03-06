# Generated by Django 3.0.7 on 2020-11-25 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_register', '0048_auto_20201124_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='antac_id',
            field=models.PositiveIntegerField(blank=True, db_index=True, default=None, null=True, unique=True, verbose_name='id from ANTAC`s DB'),
        ),
        migrations.AddField(
            model_name='companylinkwithpep',
            name='category',
            field=models.CharField(blank=True, choices=[('bank_customer', 'Bank_customer'), ('owner', 'Owner'), ('manager', 'Manager'), ('other', 'Other')], default=None, max_length=15, null=True, verbose_name='категорія'),
        ),
        migrations.AddField(
            model_name='historicalcompany',
            name='antac_id',
            field=models.PositiveIntegerField(blank=True, db_index=True, default=None, null=True, verbose_name='id from ANTAC`s DB'),
        ),
    ]
