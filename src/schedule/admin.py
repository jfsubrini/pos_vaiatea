# -*- coding: utf-8 -*-
# pylint: disable=missing-class-docstring
"""All the admin pages to create, update, delete and read the trips and guests.
    """
from django.contrib import admin
from .models import Guest, Trip


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    exclude = ("user_id",)
    list_display = ("last_name", "first_name", "gender", "nationality")
    list_filter = ("trips",)
    ordering = ("last_name", "first_name")
    search_fields = ("last_name", "first_name")

    def save_model(self, request, obj, form, change):
        obj.user_id = request.user
        super().save_model(request, obj, form, change)


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    exclude = ("user_id",)
    list_display = ("itinerary", "duration_days",
                    "starting_date", "ending_date")
    list_filter = ("starting_date",)
    ordering = ("starting_date",)
    search_fields = ("itinerary",)

    def save_model(self, request, obj, form, change):
        obj.user_id = request.user
        super().save_model(request, obj, form, change)
