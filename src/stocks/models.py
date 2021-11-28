# -*- coding: utf-8 -*-
# pylint: disable=too-few-public-methods,missing-class-docstring
"""All the models for the stocks app of the pos_vaiatea project.

    Models: Item, Drink, Goodies, Food and Stock.
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
TYPE_OF_ITEM = (
    ("Bootle & Can", "Bootle & Can"),
    ("Food", "Food"),
    ("Goodies", "Goodies"),
)


class Item(models.Model):
    """
    To create the Abstract Base Class named Item for the children Bar, Goodies, Kitchen \
        and Miscellaneous to inheritate.
    """

    name = models.CharField("Nom de l'article", max_length=30)
    price_unit_dollar = models.DecimalField(
        "Prix de vente unitaire en dollar (USD)", max_digits=5, decimal_places=2)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                related_name="%(app_label)s_%(class)s_related", verbose_name="Utilisateur")
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
        ordering = ["bar_category", "name"]

    def __str__(self):
        return f"Boisson du bar : {self.name}"


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
        verbose_name = "Goodies"
        ordering = ["goodies_category", "name"]

    def __str__(self):
        return f"Goodies : {self.name}"


class Kitchen(Item):
    """
    To create the Kitchen table that inherits from the Item abstract base class.
    Gathering data for each food item.
    """

    food_category = models.CharField(
        "Catégorie de nourriture", max_length=20, choices=KITCHEN_CATEGORY)
    price_unit_dollar = None

    class Meta:
        verbose_name = "Nourriture de la cuisine"
        ordering = ["food_category", "name"]

    def __str__(self):
        return f"Nourriture de la cuisine : {self.name}"


class Miscellaneous(Item):
    """
    To create the Miscellaneous table that inherits from the Item abstract base class.
    Gathering data for each miscellaneous item.
    """

    class Meta:
        verbose_name = "Autre article divers"
        ordering = ["name"]

    def __str__(self):
        return f"Article divers : {self.name}"


class Stock(models.Model):
    """To create the Stock table."""

    type_of_item = models.CharField(
        "Type d'article", max_length=20, choices=TYPE_OF_ITEM)
    quantity = models.PositiveSmallIntegerField(
        "Quantité", blank=True, null=True)
    # item = models.ForeignKey(
    #     Item, on_delete=models.CASCADE, related_name="stocks", verbose_name="Article")
    trips = models.ManyToManyField(
        Trip, related_name="stocks", verbose_name="Voyage")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Stock"

    def __str__(self):
        return f"Stock de catégorie {self.type_of_item}"
