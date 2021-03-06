# Generated by Django 3.0.7 on 2020-12-11 19:51
from django.db import migrations, models
from django.utils import timezone


def set_invoices_info(apps, schema):
    Invoice = apps.get_model('payment_system', 'Invoice')
    for invoice in Invoice.objects.all():
        p2s = invoice.project_subscription
        invoice.start_date = p2s.start_date
        invoice.end_date = p2s.start_date + timezone.timedelta(days=p2s.duration)
        invoice.requests_limit = p2s.subscription.requests_limit
        invoice.subscription_name = p2s.subscription.name
        invoice.project_name = p2s.project.name
        invoice.price = p2s.subscription.price
        invoice.is_custom_subscription = p2s.subscription.is_custom
        invoice.save()


class Migration(migrations.Migration):

    dependencies = [
        ('payment_system', '0025_auto_20201211_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='end_date',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='is_custom_subscription',
            field=models.BooleanField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='price',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='project_name',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='requests_limit',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='start_date',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='subscription_name',
            field=models.CharField(default=None, max_length=200, null=True),
        ),

        migrations.RunPython(
            code=set_invoices_info,
            reverse_code=migrations.RunPython.noop,
        ),

        migrations.AlterField(
            model_name='invoice',
            name='end_date',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='is_custom_subscription',
            field=models.BooleanField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='price',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='project_name',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='requests_limit',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='start_date',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='subscription_name',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='note',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='projectsubscription',
            name='subscription',
            field=models.ForeignKey(on_delete=models.deletion.PROTECT, related_name='project_subscriptions',
                                    to='payment_system.Subscription'),
        ),
    ]
