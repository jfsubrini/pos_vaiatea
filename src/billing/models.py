# -*- coding: utf-8 -*-
# pylint: disable=too-few-public-methods,missing-class-docstring
"""All the models for the billing app of the pos_vaiatea project.

    Models: Order and User.   # TODO
    """
from django.conf import settings
from django.db import models

from schedule.models import Guest

PAYMENT_MODE = (
    ("Cash USD", "Cash USD"),
    ("Cash EUR", "Cash EUR"),
    ("Cash IDR", "Cash IDR"),
    ("Credit Card", "Credit Card"),
)


class Order(models.Model):
    """
    To create the Order table in the database.
    Gathering all data for each order from a guest during the trip.
    """

    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="orders", verbose_name="Utilisateur")
    guest_id = models.ForeignKey(
        Guest, on_delete=models.CASCADE, related_name="orders", verbose_name="Passager")
    # order_line = models.ManyToManyField(
    #     Item, related_name="orders", verbose_name="commande")  # TODO
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

    order_id = models.OneToOneField(
        Order, on_delete=models.CASCADE, verbose_name="Commande")
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="payments", verbose_name="Utilisateur")
    payment_mode = models.CharField(
        "Mode de paiement", max_length=20, choices=PAYMENT_MODE)
    payment_done = models.BooleanField("Paiement effectué")
    date = models.DateTimeField("Date de la commande", auto_now=True)

    class Meta:
        verbose_name = "Paiement"

    def __str__(self):
        return f"Paiement de la commande {self.order_id} par {self.payment_mode}"
