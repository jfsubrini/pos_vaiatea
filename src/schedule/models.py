# -*- coding: utf-8 -*-
# pylint: disable=too-few-public-methods,missing-class-docstring
"""All the models for the schedule app of the pos_vaiatea project.

    Models: Guest and Trip.
    """
from django.conf import settings
from django.db import models


GENDER = (
    ("M", "M"),
    ("F", "F"),
)
NATIONALITY = (
    ("Français.e", "Français.e"),
    ("Anglais.e", "Anglais.e"),
    ("Allemand.e", "Allemand.e"),
    ("Belge", "Belge"),
    ("Suisse", "Suisse"),
    ("Néerlandais.e", "Néerlandais.e"),
    ("Italien.ne", "Italien.ne"),
    ("Espagnol.e", "Espagnol.e"),
    ("Autre Europe", "Autre Europe"),
    ("Nord-Américain.e", "Nord-Américain.e"),
    ("Canadien.ne", "Canadien.ne"),
    ("Autre Monde", "Autre Monde"),
)
DIVING_LEVEL = (
    ("Open Water", "Open Water"),
    ("Advanced OW", "Advanced OW"),
    ("Rescue Diver", "Rescue Diver"),
    ("Divemaster", "Divemaster"),
    ("Instructor", "Instructor"),
    ("Master Scuba Diver", "Master Scuba Diver"),
)


class Trip(models.Model):
    """
    To create the Trip table in the database.
    Gathering all data for each liveaboard trip.
    """

    itinerary = models.CharField(
        "Itinéraire du voyage", max_length=50)
    duration_days = models.PositiveSmallIntegerField(
        "Durée du voyage en jours")
    # présenter pour starting_date et ending_date les dates de la maniere : dd/mm/yy TODO
    starting_date = models.DateField("Date de départ du voyage", unique=True)
    ending_date = models.DateField("Date d'arrivée du voyage", unique=True)
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
        related_name="trips", verbose_name="Utilisateur")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Voyage"
        ordering = ["starting_date"]

    def __str__(self):
        formated_date = self.starting_date.strftime("%d %b %Y")
        return f"Voyage {self.itinerary} partant le {formated_date}"


class Guest(models.Model):
    """
    To create the Guest table in the database.
    Gathering all the personal data of the guest.
    """

    first_name = models.CharField("Prénom", max_length=40)
    last_name = models.CharField("Nom", max_length=40)
    gender = models.CharField(
        "Genre", max_length=10, choices=GENDER)
    age = models.PositiveSmallIntegerField(
        "Age")
    nationality = models.CharField(
        "Nationalité", max_length=25, choices=NATIONALITY)
    passport_number = models.CharField(
        "Numéro de passeport", max_length=15, unique=True, blank=True, null=True)
    diving_level = models.CharField(
        "Niveau de plongée", max_length=20, choices=DIVING_LEVEL)
    dives_number = models.PositiveSmallIntegerField(
        "Nombre de plongées", blank=True, null=True)
    email = models.EmailField(
        "Email", max_length=100)
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
        related_name="guests", verbose_name="Utilisateur")
    trips = models.ManyToManyField(
        Trip, related_name="guests", verbose_name="Voyage choisi")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Passager.ère"
        ordering = ["last_name", "first_name"]
        unique_together = (("first_name", "last_name"),)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
