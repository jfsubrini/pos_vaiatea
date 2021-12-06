# -*- coding: utf-8 -*-
# pylint: disable=too-few-public-methods,missing-class-docstring
"""All the models for the billing app of the pos_vaiatea project.

    Models: OrderLine, Bill and Payment.
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


class Bill(models.Model):
    """
    To create the Bill table in the database.
    Gathering all guest's order(s), at the end of the trip, to make the bill.
    """

    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
        related_name="bills", verbose_name="Utilisateur")
    amount = models.DecimalField(
        "Montant de la facture", max_digits=5, decimal_places=2)
    bill_date = models.DateTimeField("Date de la facture", auto_now=True)

    class Meta:
        verbose_name = "Facture"

    # def __str__(self):
        # return f"Facture du passager.ère {self.guest_id}"  # TODO


class OrderLine(models.Model):
    """
    To create the OrderLine table in the database.
    Gathering all data for each line of order from a guest during the trip.
    """

    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
        related_name="orderlines", verbose_name="Utilisateur")
    guest_id = models.ForeignKey(
        Guest, on_delete=models.CASCADE, related_name="orderlines", verbose_name="Passager.ère")
    bar_id = models.ForeignKey(
        Bar, on_delete=models.PROTECT, blank=True, null=True,
        related_name="orderlines", verbose_name="Boisson de bar")
    goodies_id = models.ForeignKey(
        Goodies, on_delete=models.PROTECT, blank=True, null=True,
        related_name="orderlines", verbose_name="Goodies")
    miscellaneous_id = models.ForeignKey(
        Miscellaneous, on_delete=models.PROTECT, blank=True, null=True,
        related_name="orderlines", verbose_name="Autre article divers")
    bill_id = models.ForeignKey(
        Bill, on_delete=models.SET_NULL, blank=True, null=True,
        related_name="orderlines", verbose_name="Facture")
    quantity = models.PositiveSmallIntegerField("Quantité")
    order_date = models.DateTimeField("Date de la commande", auto_now=True)

    class Meta:
        verbose_name = "Commande"

    def __str__(self):
        return f"Commande d'un article par {self.guest_id}"


class Payment(models.Model):
    """
    To create the Payment table in the database.
    Mode of payment for each bill, at the end of the trip.
    """

    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
        related_name="payments", verbose_name="Utilisateur")
    bill_id = models.ForeignKey(
        Bill, on_delete=models.PROTECT, related_name="payments", verbose_name="Facture")
    payment_mode = models.CharField(
        "Mode de paiement", max_length=20, choices=PAYMENT_MODE)
    payment_date = models.DateTimeField("Date de la commande", auto_now=True)

    class Meta:
        verbose_name = "Paiement"

    def __str__(self):
        return f"Paiement de la facture {self.bill_id} par {self.payment_mode}"
