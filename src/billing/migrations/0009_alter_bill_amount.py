# Generated by Django 3.2.9 on 2021-12-13 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0008_auto_20211212_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Montant de la facture'),
        ),
    ]
