# Generated by Django 3.2.9 on 2021-12-12 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0007_alter_orderline_trip_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillPaid',
            fields=[
            ],
            options={
                'verbose_name': 'Facture payée',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('billing.bill',),
        ),
        migrations.CreateModel(
            name='InvoicedOrder',
            fields=[
            ],
            options={
                'verbose_name': 'Commande facturée',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('billing.orderline',),
        ),
        migrations.AddField(
            model_name='bill',
            name='payment_done',
            field=models.BooleanField(default=False, verbose_name='Facture payée'),
        ),
    ]