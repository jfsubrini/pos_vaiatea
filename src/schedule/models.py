# -*- coding: utf-8 -*-
# pylint: disable=too-few-public-methods,missing-class-docstring
"""All the models for the schedule app of the pos_vaiatea project.

    Models: Guest and Trip.
    """
from django.conf import settings
from django.db import models


GENDER = (
    ("Male", "Male"),
    ("Female", "Female"),
)
DIVING_LEVEL = (
    ("Open Water", "Open Water"),
    ("Advanced OW", "Advanced OW"),
    ("Rescue Diver", "Rescue Diver"),
    ("Divemaster", "Divemaster"),
    ("Instructor", "Instructor"),
    ("Master Scuba Diver", "Master Scuba Diver"),
)


class Guest(models.Model):
    """To create the Guest table."""

    first_name = models.CharField("Prénom", max_length=40)
    last_name = models.CharField("Nom", max_length=40)
    gender = models.CharField(
        "Genre", max_length=10, choices=GENDER)
    age = models.PositiveSmallIntegerField(
        "Age")
    nationality = models.CharField(
        "Nationalité", max_length=30)
    passport_number = models.CharField(
        "Numéro de passeport", max_length=15, blank=True, null=True)
    diving_level = models.CharField(
        "Niveau de plongée", max_length=20, choices=DIVING_LEVEL)
    dives_number = models.PositiveSmallIntegerField(
        "Nombre de plongées", blank=True, null=True)
    email = models.CharField(
        "Email", max_length=100)

    class Meta:
        verbose_name = "Invité(e)"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Trip(models.Model):
    """To create the Trip table."""

    itinerary = models.CharField(
        "Itinéraire du liveaboard", max_length=40)
    duration_days = models.PositiveSmallIntegerField(
        "Durée en jours")
    starting_date = models.DateField("Date de départ du liveaboard")
    ending_date = models.DateField("Date d'arrivée du liveaboard")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="trips")
    guests = models.ManyToManyField(
        Guest, related_name="trips", verbose_name="voyage")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Voyage"

    def __str__(self):
        return f"Voyage {self.itinerary}"
