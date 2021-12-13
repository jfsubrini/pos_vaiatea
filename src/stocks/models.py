# -*- coding: utf-8 -*-
# pylint: disable=too-few-public-methods,missing-class-docstring
"""All the models for the stocks app of the pos_vaiatea project.

    Models: Item, Bar, Goodies, Kitchen, Miscellaneous and Stock.
    """
from django.conf import settings
from django.db import models
from schedule.models import Trip


GOODIES_CATEGORY = (
    ("Tee-Shirt", "Tee-Shirt"),
    ("Sweat-Shirt", "Sweat-Shirt"),
    ("Cap", "Cap"),
    ("Autre", "Autre"),
)
SIZE = (
    ("XS", "XS"),
    ("S", "S"),
    ("M", "M"),
    ("L", "L"),
    ("XL", "XL"),
    ("XXL", "XXL"),
    ("Autre", "Autre"),
)
GENDER = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Unisex", "Unisex"),
)
BAR_CATEGORY = (
    ("Vins", "Vins"),
    ("Alcools", "Alcools"),
    ("Soft drinks", "Soft drinks"),
)
KITCHEN_CATEGORY = (
    ("Viande", "Viande"),
    ("Poisson", "Poisson"),
    ("Légumes", "Légumes"),
    ("Fruits", "Fruits"),
    ("Boites", "Boites"),
    ("Surgelés", "Surgelés"),
    ("Epices", "Epices"),
    ("Farine", "Farine"),
    ("Lait", "Lait"),
    ("Café & Thé", "Café & Thé"),
    ("Autre épicerie", "Autre épicerie"),
    ("Autre", "Autre"),
)


class Item(models.Model):
    """
    To create the Abstract Base Class named Item for the children Bar, Goodies, Kitchen \
        and Miscellaneous to inheritate.
    """

    name = models.CharField("Nom de l'article", max_length=30)
    price_unit_dollar = models.DecimalField(
        "Prix de vente unitaire en dollar (USD)", max_digits=6, decimal_places=2)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True,
                                on_delete=models.SET_NULL,
                                related_name="%(app_label)s_%(class)s_related",
                                verbose_name="Utilisateur")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Bar(Item):
    """
    To create the Bar table that inherits from the Item abstract base class.
    Gathering data for each drink item.
    """

    bar_category = models.CharField(
        "Catégorie du bar", max_length=20, choices=BAR_CATEGORY)

    class Meta:
        verbose_name = "Boisson du bar"
        verbose_name_plural = "Boissons du bar"
        ordering = ["bar_category", "name"]

    def __str__(self):
        return f"{self.name} à {self.price_unit_dollar}"


class Goodies(Item):
    """
    To create the Goodies table that inherits from the Item abstract base class.
    Gathering data for each goodies item.
    """

    goodies_category = models.CharField(
        "Catégorie de goodies", max_length=20, choices=GOODIES_CATEGORY)
    size = models.CharField(
        "Taille", max_length=5, choices=SIZE)
    color = models.CharField(
        "Couleur", max_length=30)
    gender = models.CharField(
        "Genre", max_length=10, choices=GENDER)

    class Meta:
        verbose_name = "Goody"
        verbose_name_plural = "Goodies"
        ordering = ["goodies_category", "name"]

    def __str__(self):
        return f"{self.goodies_category} {self.name} à {self.price_unit_dollar} USD"


class Kitchen(Item):
    """
    To create the Kitchen table that inherits from the Item abstract base class.
    Gathering data for each food item.
    """

    food_category = models.CharField(
        "Catégorie de nourriture", max_length=20, choices=KITCHEN_CATEGORY)
    price_unit_dollar = None

    class Meta:
        verbose_name = "Nourriture"
        ordering = ["food_category", "name"]

    def __str__(self):
        return f"{self.food_category} {self.name}"


class Miscellaneous(Item):
    """
    To create the Miscellaneous table that inherits from the Item abstract base class.
    Gathering data for each miscellaneous item.
    """

    class Meta:
        verbose_name = "Autre article divers"
        verbose_name_plural = "Autres articles divers"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} à {self.price_unit_dollar} USD"


class Stock(models.Model):
    """To create the Stock table."""

    bar_initial_id = models.ForeignKey(
        Bar, blank=True, null=True, on_delete=models.PROTECT,
        related_name="%(app_label)s_%(class)s_initial_related",
        verbose_name="stock initial de boisson")
    bar_final_id = models.ForeignKey(
        Bar, blank=True, null=True, on_delete=models.PROTECT,
        related_name="%(app_label)s_%(class)s_final_related",
        verbose_name="stock final de boisson")
    goodies_initial_id = models.ForeignKey(
        Goodies, blank=True, null=True, on_delete=models.PROTECT,
        related_name="%(app_label)s_%(class)s_initial_related",
        verbose_name="stock initial de goodies")
    goodies_final_id = models.ForeignKey(
        Goodies, blank=True, null=True, on_delete=models.PROTECT,
        related_name="%(app_label)s_%(class)s_final_related",
        verbose_name="stock final de goodies")
    kitchen_initial_id = models.ForeignKey(
        Kitchen, blank=True, null=True, on_delete=models.PROTECT,
        related_name="%(app_label)s_%(class)s_initial_related",
        verbose_name="stock initial de nourriture")
    kitchen_final_id = models.ForeignKey(
        Kitchen, blank=True, null=True, on_delete=models.PROTECT,
        related_name="%(app_label)s_%(class)s_final_related",
        verbose_name="stock final de nourriture")
    trip_id = models.ForeignKey(
        Trip, on_delete=models.CASCADE, related_name="stocks", verbose_name="Voyage")
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
        related_name="stocks", verbose_name="Utilisateur")
    quantity = models.PositiveSmallIntegerField(
        "Quantité", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Stock"

    def __str__(self):
        return f"Stock du voyage {self.trip_id}"


class InitialBarStock(Stock):

    class Meta:
        proxy = True
        verbose_name = "Stock initial du bar"
        verbose_name_plural = "Stocks initiaux du bar"


class FinalBarStock(Stock):

    class Meta:
        proxy = True
        verbose_name = "Stock final du bar"
        verbose_name_plural = "Stocks finaux du bar"


class InitialKitchenStock(Stock):

    class Meta:
        proxy = True
        verbose_name = "Stock initial de la cuisine"
        verbose_name_plural = "Stocks initiaux de la cuisine"


class FinalKitchenStock(Stock):

    class Meta:
        proxy = True
        verbose_name = "Stock final de la cuisine"
        verbose_name_plural = "Stocks finaux de la cuisine"


class InitialGoodiesStock(Stock):

    class Meta:
        proxy = True
        verbose_name = "Stock initial de goodies"
        verbose_name_plural = "Stocks initiaux de goodies"


class FinalGoodiesStock(Stock):

    class Meta:
        proxy = True
        verbose_name = "Stock final de goodies"
        verbose_name_plural = "Stocks finaux de goodies"
