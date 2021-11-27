# Generated by Django 3.2.9 on 2021-11-27 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0002_remove_payment_payment_done'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Montant de la facture'),
        ),
    ]
