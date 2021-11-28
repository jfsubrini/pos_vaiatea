# -*- coding: utf-8 -*-
# pylint: disable=too-few-public-methods,missing-class-docstring
"""All the models for the billing app of the pos_vaiatea project.

    Models: Order and User.   # TODO
    """
from django.conf import settings
from django.db import models

from schedule.models import Guest
from stocks.models import Bar, Goodies, Miscellaneous

PAYMENT_MODE = (
    ("Cash USD", "Cash USD"),
    ("Cash EUR", "Cash EUR"),
    ("Cash IDR", "Cash IDR"),
    ("Credit Card", "Credit Card"),
)


class OrderLine(models.Model):
    """
    To create the OrderLine table in the database.
    Gathering all data for each line of order from a guest during the trip.
    """

    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="orderlines", verbose_name="Utilisateur")
    guest_id = models.ForeignKey(
        Guest, on_delete=models.CASCADE, related_name="orderlines", verbose_name="Passager")
    bar_id = models.ForeignKey(
        Bar, on_delete=models.CASCADE, related_name="orderlines", verbose_name="Boisson de bar")
    goodies_id = models.ForeignKey(
        Goodies, on_delete=models.CASCADE, related_name="orderlines", verbose_name="Goodies")
    miscellaneous_id = models.ForeignKey(
        Miscellaneous, on_delete=models.CASCADE, related_name="orderlines", verbose_name="Autre article divers")
    quantity = models.PositiveSmallIntegerField("Quantité")
    date = models.DateTimeField("Date de la commande", auto_now=True)

    class Meta:
        verbose_name = "Commande"

    def __str__(self):
        #  TODO changer au nom de l'article
        return f"Commande du passager : {self.guest_id}"


class Payment(models.Model):
    """
    To create the Payment table in the database.
    Gathering all data for each payment, for guest's order(s), at the end of the trip.
    """

    orders = models.ManyToManyField(
        OrderLine, related_name="payments", verbose_name="Commande")
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="payments", verbose_name="Utilisateur")
    amount = models.DecimalField(
        "Montant de la facture", max_digits=5, decimal_places=2)
    payment_mode = models.CharField(
        "Mode de paiement", max_length=20, choices=PAYMENT_MODE)
    date = models.DateTimeField("Date de la commande", auto_now=True)
    orders = models.ManyToManyField(
        OrderLine, related_name="payments", verbose_name="commande")

    class Meta:
        verbose_name = "Paiement"

    def __str__(self):
        return f"Paiement de la commande {self.order_id} par {self.payment_mode}"
