# -*- coding: utf-8 -*-
# pylint: disable=too-few-public-methods,missing-class-docstring
"""All the models for the stocks app of the pos_vaiatea project.

    Models: Item, Drink, Goodies, Food and Stock.
    """
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
FOOD_CATEGORY = (
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


class Drink(models.Model):
    """
    To create the Drink table.
    Gathering data for each drink item.
    """

    price_unit_dollar = models.DecimalField(
        "Prix de vente unitaire en dollar (USD)", max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = "Boisson"

    def __str__(self):
        return f"Boisson au prix unitaire de vente en dollar (USD) de {self.price_unit_dollar}"


class Goodies(models.Model):
    """
    To create the Goodies table.
    Gathering data for each goodies item.
    """

    category = models.CharField(
        "Catégorie", max_length=20, choices=GOODIES_CATEGORY)
    size = models.CharField(
        "Taille", max_length=5, choices=SIZE)
    color = models.CharField(
        "Couleur", max_length=30)
    gender = models.CharField(
        "Genre", max_length=10, choices=GENDER)
    price_unit_dollar = models.DecimalField(
        "Prix de vente unitaire en dollar (USD)", max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = "Goodies"

    def __str__(self):
        return f"Goodies de catégorie {self.category}"


class Food(models.Model):
    """
    To create the Food table.
    Gathering data for each food item.
    """

    food_category = models.CharField(
        "Catégorie de nourriture", max_length=20, choices=FOOD_CATEGORY)

    class Meta:
        verbose_name = "Nourriture"

    def __str__(self):
        return f"Nourriture de type {self.food_category}"


class Miscellaneous(models.Model):
    """
    To create the Miscellaneous table.
    Gathering data for each miscellaneous item.
    """

    price_unit_dollar = models.DecimalField(
        "Prix de vente unitaire en dollar (USD)", max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = "Autre article divers"

    def __str__(self):
        return f"Article divers au prix unitaire de vente en dollar (USD) de {self.price_unit_dollar}"


class Item(models.Model):
    """
    To create the Item table.
    Gathering the name for each drink, goodies, food or miscellaneous item.
    """

    name = models.CharField("Nom de l'article", max_length=30)
    drink = models.OneToOneField(
        Drink, on_delete=models.CASCADE, verbose_name="Boisson")
    goodies = models.OneToOneField(
        Goodies, on_delete=models.CASCADE, verbose_name="Goodies")
    food = models.OneToOneField(
        Food, on_delete=models.CASCADE, verbose_name="Nourriture")
    miscellaneous = models.OneToOneField(
        Miscellaneous, on_delete=models.CASCADE, verbose_name="Autre article divers")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Article"

    def __str__(self):
        return f"Article nommé {self.name}"


class Stock(models.Model):
    """To create the Stock table."""

    type_of_item = models.CharField(
        "Type d'article", max_length=20, choices=TYPE_OF_ITEM)
    quantity = models.PositiveSmallIntegerField(
        "Quantité", blank=True, null=True)
    item = models.ForeignKey(
        Item, on_delete=models.CASCADE, related_name="stocks", verbose_name="Article")
    trips = models.ManyToManyField(
        Trip, related_name="stocks", verbose_name="Voyage")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Stock"

    def __str__(self):
        return f"Stock de catégorie {self.type_of_item}"
