# Generated by Django 3.2.9 on 2021-12-01 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0003_auto_20211201_1640'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='miscellaneous',
            options={'ordering': ['name'], 'verbose_name': 'Autre'},
        ),
    ]
