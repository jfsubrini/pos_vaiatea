# Generated by Django 3.2.9 on 2021-11-27 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodies',
            name='goodies_category',
            field=models.CharField(choices=[('Tee-Shirt', 'Tee-Shirt'), ('Sweat-Shirt', 'Sweat-Shirt'), ('Cap', 'Cap'), ('Autre', 'Autre')], max_length=20, verbose_name='Catégorie de goodies'),
        ),
    ]