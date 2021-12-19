# Generated by Django 3.2.9 on 2021-12-18 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0012_alter_rate_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='credit_card_fee',
            field=models.DecimalField(decimal_places=4, max_digits=5, unique=True, verbose_name='Frais de carte de crédit'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='usd_eur',
            field=models.DecimalField(decimal_places=4, max_digits=6, unique=True, verbose_name='Taux de change USD-EUR'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='usd_idr',
            field=models.PositiveSmallIntegerField(unique=True, verbose_name='Taux de change USD-IDR'),
        ),
    ]
