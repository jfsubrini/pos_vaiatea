# Generated by Django 3.2.9 on 2021-12-09 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0005_initialbarstock'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinalBarStock',
            fields=[
            ],
            options={
                'verbose_name': 'Stock final du bar',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('stocks.stock',),
        ),
        migrations.CreateModel(
            name='FinalGoodiesStock',
            fields=[
            ],
            options={
                'verbose_name': 'Stock final de goodies',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('stocks.stock',),
        ),
        migrations.CreateModel(
            name='FinalKitchenStock',
            fields=[
            ],
            options={
                'verbose_name': 'Stock final de la cuisine',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('stocks.stock',),
        ),
        migrations.CreateModel(
            name='InitialGoodiesStock',
            fields=[
            ],
            options={
                'verbose_name': 'Stock initial de goodies',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('stocks.stock',),
        ),
        migrations.CreateModel(
            name='InitialKitchenStock',
            fields=[
            ],
            options={
                'verbose_name': 'Stock initial de la cuisine',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('stocks.stock',),
        ),
    ]