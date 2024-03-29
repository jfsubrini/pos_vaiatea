# Generated by Django 3.2.9 on 2021-12-13 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0006_finalbarstock_finalgoodiesstock_finalkitchenstock_initialgoodiesstock_initialkitchenstock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bar',
            name='price_unit_dollar',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Prix de vente unitaire en dollar (USD)'),
        ),
        migrations.AlterField(
            model_name='goodies',
            name='price_unit_dollar',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Prix de vente unitaire en dollar (USD)'),
        ),
        migrations.AlterField(
            model_name='miscellaneous',
            name='price_unit_dollar',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Prix de vente unitaire en dollar (USD)'),
        ),
    ]
