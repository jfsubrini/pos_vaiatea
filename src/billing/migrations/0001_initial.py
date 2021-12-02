# Generated by Django 3.2.9 on 2021-12-02 08:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stocks', '0001_initial'),
        ('schedule', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Montant de la facture')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Date de la commande')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bills', to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur')),
            ],
            options={
                'verbose_name': 'Paiement',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_mode', models.CharField(choices=[('Cash USD', 'Cash USD'), ('Cash EUR', 'Cash EUR'), ('Cash IDR', 'Cash IDR'), ('Credit Card', 'Credit Card')], max_length=20, verbose_name='Mode de paiement')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Date de la commande')),
                ('bill_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='payments', to='billing.bill', verbose_name='Facture')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payments', to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur')),
            ],
            options={
                'verbose_name': 'Paiement',
            },
        ),
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(verbose_name='Quantité')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Date de la commande')),
                ('bar_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orderlines', to='stocks.bar', verbose_name='Boisson de bar')),
                ('bill_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orderlines', to='billing.bill', verbose_name='Facture')),
                ('goodies_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orderlines', to='stocks.goodies', verbose_name='Goodies')),
                ('guest_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderlines', to='schedule.guest', verbose_name='Passager.ère')),
                ('miscellaneous_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orderlines', to='stocks.miscellaneous', verbose_name='Autre article divers')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orderlines', to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur')),
            ],
            options={
                'verbose_name': 'Commande',
            },
        ),
    ]
