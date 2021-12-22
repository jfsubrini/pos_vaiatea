# -*- coding: utf-8 -*-
# pylint: disable=missing-class-docstring, no-member
"""All the admin pages to create, update, delete and read the trips and guests.
    """
from datetime import timedelta
from rangefilter.filter import DateRangeFilter
from django.contrib import admin
from .models import Guest, Trip


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    exclude = ("user_id",)
    list_display = ("last_name", "first_name", "gender",
                    "nationality", "show_trip")
    list_filter = ("trips",)
    ordering = ("last_name", "first_name")
    search_fields = ("last_name", "first_name")

    def show_trip(self, obj):
        guest_trip = Trip.objects.filter(guests=obj).first()
        trip_name = guest_trip.itinerary
        return trip_name

    show_trip.short_description = "Voyage"

    def save_model(self, request, obj, form, change):
        obj.user_id = request.user
        super().save_model(request, obj, form, change)


@ admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    exclude = ("user_id", "ending_date")
    list_display = ("itinerary", "duration_days",
                    "starting_date", "ending_date")
    list_filter = (('starting_date', DateRangeFilter),)
    ordering = ("starting_date",)
    search_fields = ("itinerary",)

    def save_model(self, request, obj, form, change):
        obj.user_id = request.user
        obj.ending_date = form.cleaned_data.get('starting_date') + \
            timedelta(days=form.cleaned_data.get('duration_days') - 1)
        super().save_model(request, obj, form, change)
