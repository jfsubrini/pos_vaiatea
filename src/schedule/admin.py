from django.contrib import admin
from .models import Guest, Trip


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "gender", "age", "nationality",
                    "diving_level", "dives_number", "email", "passport_number")
    ordering = ("last_name", "first_name")
    # rajouter en premier le tri par trip id si possible TODO
    search_fields = ("last_name", "first_name", "nationality")
    # enlever user_id field # TODO
    # présenter les dates de la maniere : dd/mm/yy TODO
    # "trips" faire apparaitre le voyage dans la liste TODO
    # ne pas pouvoir choisir plusieurs voyages et ne pas pouvoir créer un voyage depuis guest. TODO
    # ne pas pouvoir modifier un user et ne pas pouvoir créer un user depuis guest. TODO


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    # WARNING : When creating the trips, do it following the order of the starting date.
    list_display = ("itinerary", "duration_days",
                    "starting_date", "ending_date")
    ordering = ("starting_date",)
    search_fields = ("itinerary",)
    # enlever user_id field # TODO
    # présenter les dates de la maniere : dd/mm/yy TODO
    # ne pas pouvoir modifier un user et ne pas pouvoir créer un user depuis guest. TODO
