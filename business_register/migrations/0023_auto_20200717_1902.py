# Generated by Django 3.0.7 on 2020-07-17 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_register', '0022_auto_20200717_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='founderfull',
            name='address',
            field=models.CharField(max_length=2015, null=True),
        ),
        migrations.AlterField(
            model_name='historicalfounderfull',
            name='address',
            field=models.CharField(max_length=2015, null=True),
        ),
    ]
