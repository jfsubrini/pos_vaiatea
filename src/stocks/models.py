# -*- coding: utf-8 -*-
# pylint: disable=too-few-public-methods,missing-class-docstring
"""All the models for the stocks app of the pos_vaiatea project.

    Models: Item, Drink, Goodies, Food and Stock.
    """
from django.db import models
from schedule.models import Trip


CATEGORY = (
    ("Tee-Shirt", "Tee-Shirt"),
    ("Sweat-Shirt", "Sweat-Shirt"),
    ("Cap", "Cap"),
)
SIZE = (
    ("XS", "XS"),
    ("S", "S"),
    ("M", "M"),
    ("L", "L"),
    ("XL", "XL"),
    ("XXL", "XXL"),
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
    ("Blabla", "Blabla"),
)
TYPE_OF_ITEM = (
    ("Bootle & Can", "Bootle & Can"),
    ("Food", "Food"),
    ("Goodies", "Goodies"),
)


class Drink(models.Model):
    """To create the Drink table."""

    price_unit_dollar = models.DecimalField(
        "Prix unitaire en dollar", max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = "Boisson"

    def __str__(self):
        return f"Boisson au prix unitaire en dollar de {self.price_unit_dollar}"


class Goodies(models.Model):
    """To create the Goodies table."""

    category = models.CharField(
        "Catégorie", max_length=20, choices=CATEGORY)
    size = models.CharField(
        "Taille", max_length=5, choices=SIZE)
    color = models.CharField(
        "Couleur", max_length=30)
    gender = models.CharField(
        "Genre", max_length=10, choices=GENDER)
    price_unit_dollar = models.DecimalField(
        "Prix unitaire en dollar", max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = "Goodies"

    def __str__(self):
        return f"Goodies de catégorie {self.category}"


class Food(models.Model):
    """To create the Food table."""

    food_category = models.CharField(
        "Catégorie de nourriture", max_length=20, choices=FOOD_CATEGORY)

    class Meta:
        verbose_name = "Nourriture"

    def __str__(self):
        return f"Nourriture de catégorie {self.food_category}"


class Item(models.Model):
    """To create the Item table."""

    name = models.CharField("Nom de l'article", max_length=30)
    drink = models.OneToOneField(
        Drink, on_delete=models.CASCADE, verbose_name="Boisson")
    goodies = models.OneToOneField(
        Goodies, on_delete=models.CASCADE, verbose_name="Goodies")
    food = models.OneToOneField(
        Food, on_delete=models.CASCADE, verbose_name="Nourriture")
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
        Trip, related_name="stocks", verbose_name="stock")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Stock"

    def __str__(self):
        return f"Stock de catégorie {self.type_of_item}"
