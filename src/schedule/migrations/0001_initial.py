# Generated by Django 3.2.9 on 2021-11-29 09:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itinerary', models.CharField(max_length=50, verbose_name='Itinéraire du voyage')),
                ('duration_days', models.PositiveSmallIntegerField(choices=[(1, 6), (2, 7), (3, 8), (4, 9), (5, 10), (6, 11), (7, 12), (8, 13), (9, 14), (10, 15), (11, 16), (12, 17), (13, 18), (14, 19), (15, 20), (16, 21)], verbose_name='Durée du voyage en jours')),
                ('starting_date', models.DateField(unique=True, verbose_name='Date de départ du voyage')),
                ('ending_date', models.DateField(unique=True, verbose_name="Date d'arrivée du voyage")),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips', to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur')),
            ],
            options={
                'verbose_name': 'Voyage',
                'ordering': ['starting_date'],
            },
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40, verbose_name='Prénom')),
                ('last_name', models.CharField(max_length=40, verbose_name='Nom')),
                ('gender', models.CharField(choices=[('Homme', 'Homme'), ('Femme', 'Femme')], max_length=10, verbose_name='Genre')),
                ('age', models.PositiveSmallIntegerField(verbose_name='Age')),
                ('nationality', models.CharField(choices=[('Français.e', 'Français.e'), ('Anglais.e', 'Anglais.e'), ('Allemand.e', 'Allemand.e'), ('Belge', 'Belge'), ('Suisse', 'Suisse'), ('Néerlandais.e', 'Néerlandais.e'), ('Italien.ne', 'Italien.ne'), ('Espagnol.e', 'Espagnol.e'), ('Autre Europe', 'Autre Europe'), ('Nord-Américain.e', 'Nord-Américain.e'), ('Canadien.ne', 'Canadien.ne'), ('Autre Monde', 'Autre Monde')], max_length=25, verbose_name='Nationalité')),
                ('passport_number', models.CharField(blank=True, max_length=15, null=True, unique=True, verbose_name='Numéro de passeport')),
                ('diving_level', models.CharField(choices=[('Open Water', 'Open Water'), ('Advanced OW', 'Advanced OW'), ('Rescue Diver', 'Rescue Diver'), ('Divemaster', 'Divemaster'), ('Instructor', 'Instructor'), ('Master Scuba Diver', 'Master Scuba Diver')], max_length=20, verbose_name='Niveau de plongée')),
                ('dives_number', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Nombre de plongées')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('trips', models.ManyToManyField(related_name='guests', to='schedule.Trip', verbose_name='Voyage choisi')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guests', to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur')),
            ],
            options={
                'verbose_name': 'Passager.ère',
                'ordering': ['last_name', 'first_name'],
            },
        ),
    ]
