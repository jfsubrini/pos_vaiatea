# Generated by Django 3.2.9 on 2021-11-26 20:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schedule', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(verbose_name='Quantité')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Date de la commande')),
                ('guest_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='schedule.guest', verbose_name='Passager')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur')),
            ],
            options={
                'verbose_name': 'Commande',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_mode', models.CharField(choices=[('Cash USD', 'Cash USD'), ('Cash EUR', 'Cash EUR'), ('Cash IDR', 'Cash IDR'), ('Credit Card', 'Credit Card')], max_length=20, verbose_name='Mode de paiement')),
                ('payment_done', models.BooleanField(verbose_name='Paiement effectué')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Date de la commande')),
                ('order_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='billing.order', verbose_name='Commande')),
            ],
            options={
                'verbose_name': 'Paiement',
            },
        ),
    ]
