# Generated by Django 3.2.9 on 2021-11-26 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_unit_dollar', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Prix de vente unitaire en dollar (USD)')),
            ],
            options={
                'verbose_name': 'Boisson',
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_category', models.CharField(choices=[('Viande', 'Viande'), ('Poisson', 'Poisson'), ('Légumes', 'Légumes'), ('Fruits', 'Fruits'), ('Boites', 'Boites'), ('Surgelés', 'Surgelés'), ('Epices', 'Epices'), ('Farine', 'Farine'), ('Lait', 'Lait'), ('Café & Thé', 'Café & Thé'), ('Autre épicerie', 'Autre épicerie'), ('Autre', 'Autre')], max_length=20, verbose_name='Catégorie de nourriture')),
            ],
            options={
                'verbose_name': 'Nourriture',
            },
        ),
        migrations.CreateModel(
            name='Goodies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Tee-Shirt', 'Tee-Shirt'), ('Sweat-Shirt', 'Sweat-Shirt'), ('Cap', 'Cap'), ('Autre', 'Autre')], max_length=20, verbose_name='Catégorie')),
                ('size', models.CharField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'), ('Autre', 'Autre')], max_length=5, verbose_name='Taille')),
                ('color', models.CharField(max_length=30, verbose_name='Couleur')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Unisex', 'Unisex')], max_length=10, verbose_name='Genre')),
                ('price_unit_dollar', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Prix de vente unitaire en dollar (USD)')),
            ],
            options={
                'verbose_name': 'Goodies',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name="Nom de l'article")),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('drink', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='stocks.drink', verbose_name='Boisson')),
                ('food', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='stocks.food', verbose_name='Nourriture')),
                ('goodies', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='stocks.goodies', verbose_name='Goodies')),
            ],
            options={
                'verbose_name': 'Article',
            },
        ),
        migrations.CreateModel(
            name='Miscellaneous',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_unit_dollar', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Prix de vente unitaire en dollar (USD)')),
            ],
            options={
                'verbose_name': 'Autre article divers',
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_item', models.CharField(choices=[('Bootle & Can', 'Bootle & Can'), ('Food', 'Food'), ('Goodies', 'Goodies')], max_length=20, verbose_name="Type d'article")),
                ('quantity', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Quantité')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stocks', to='stocks.item', verbose_name='Article')),
                ('trips', models.ManyToManyField(related_name='stocks', to='schedule.Trip', verbose_name='Voyage')),
            ],
            options={
                'verbose_name': 'Stock',
            },
        ),
        migrations.AddField(
            model_name='item',
            name='miscellaneous',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='stocks.miscellaneous', verbose_name='Autre article divers'),
        ),
    ]
