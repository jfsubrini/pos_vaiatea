# -*- coding: utf-8 -*-
# pylint: disable=missing-class-docstring, no-member
"""All the admin pages to create, update, delete and read \
    all the bar, kitchen, goodies and miscellanous items.
    Idem for the initial and final stocks inventory of the bar, \
        kitchen and goodies items.
    """
from django.contrib import admin
from django.shortcuts import render
from .models import (
    Bar,
    Goodies,
    Kitchen,
    Miscellaneous,
    Stock,
    Trip,
)


# CUSTOM ADMIN ACTIONS
# Actions in the items' lists to make initial and final inventory of the items.
@admin.action(description='Inventaire du stock initial du bar')
def make_bar_initial_stocks(modeladmin, request, queryset):
    """ Choix dans action pour faire un inventaire du stock initial du bar \
        puis envoi vers une page intermédiaire."""
    if "apply" in request.POST:
        # Checking if the form has been validated.
        all_drinks = queryset.all()
        all_trips = Trip.objects.all()
        if all_drinks.is_valid() and all_trips.is_valid:
            # Saving the data from the initial bar stock inventory form to update the stock data into the database.
            # form = edit_draft_form.save(commit=False)
            # form.draft = selected_wallet.draft
            # form.created_at = selected_wallet.created_at
            # form.save()
            # for item in queryset:
            #     print("XXXXXXXXX : ", item.id, type(item.id))
            #     bar_initial = Stock(
            #         bar_initial_id=item.id, trip_id=1, quantity=1)
            #     bar_initial.save()
            print("XXXXXXXX HOLA XXXXXXXXX")

    # To display the stock inventory with all the drinks registered into the database
    # with the choice of trips.
    else:
        all_drinks = queryset.all()
        all_trips = Trip.objects.all()

    # What to render to the template.
    return render(request, 'admin/bar_initial_stocks.html',
                  context={"drinks": all_drinks, "trips": all_trips})


@admin.action(description='Inventaire du stock final du bar')
def make_bar_final_stocks(modeladmin, request, queryset):
    """ Choix dans action pour faire un inventaire du stock final du bar \
        puis envoi vers une page intermédiaire."""
    all_drinks = queryset.all()
    all_trips = Trip.objects.all()
    return render(request, 'admin/bar_final_stocks.html',
                  context={"drinks": all_drinks, "trips": all_trips})


@admin.action(description='Inventaire du stock initial des goodies')
def make_goodies_initial_stocks(modeladmin, request, queryset):
    """ Choix dans action pour faire un inventaire du stock initial des goodies \
        puis envoi vers une page intermédiaire."""
    all_goodies = queryset.all()
    all_trips = Trip.objects.all()
    return render(request, 'admin/goodies_initial_stocks.html',
                  context={"goodies": all_goodies, "trips": all_trips})


@admin.action(description='Inventaire du stock final des goodies')
def make_goodies_final_stocks(modeladmin, request, queryset):
    """ Choix dans action pour faire un inventaire du stock final des goodies \
        puis envoi vers une page intermédiaire."""
    all_goodies = queryset.all()
    all_trips = Trip.objects.all()
    return render(request, 'admin/goodies_final_stocks.html',
                  context={"goodies": all_goodies, "trips": all_trips})


@admin.action(description='Inventaire du stock initial en cuisine')
def make_kitchen_initial_stocks(modeladmin, request, queryset):
    """ Choix dans action pour faire un inventaire du stock initial en cuisine \
        puis envoi vers une page intermédiaire."""
    all_food = queryset.all()
    all_trips = Trip.objects.all()
    return render(request, 'admin/kitchen_initial_stocks.html',
                  context={"foods": all_food, "trips": all_trips})


@admin.action(description='Inventaire du stock final en cuisine')
def make_kitchen_final_stocks(modeladmin, request, queryset):
    """ Choix dans action pour faire un inventaire du stock final en cuisine \
        puis envoi vers une page intermédiaire."""
    all_food = queryset.all()
    all_trips = Trip.objects.all()
    return render(request, 'admin/kitchen_final_stocks.html',
                  context={"foods": all_food, "trips": all_trips})

#################################################################################


# BAR CRUD
@admin.register(Bar)
class BarAdmin(admin.ModelAdmin):
    exclude = ("user_id",)
    list_display = ("name", "price_unit_dollar", "bar_category")
    list_display_links = ("name", "price_unit_dollar")
    list_filter = ("bar_category",)
    ordering = ("name",)
    search_fields = ("name",)
    actions = [make_bar_initial_stocks, make_bar_final_stocks]

    def save_model(self, request, obj, form, change):
        obj.user_id = request.user
        super().save_model(request, obj, form, change)


# GOODIES CRUD
@admin.register(Goodies)
class GoodiesAdmin(admin.ModelAdmin):
    exclude = ("user_id",)
    list_display = ("name", "price_unit_dollar",
                    "goodies_category", "size", "color", "gender")
    list_display_links = ("name", "price_unit_dollar")
    list_filter = ("goodies_category", "size")
    ordering = ("name",)
    search_fields = ("name",)
    actions = [make_goodies_initial_stocks, make_goodies_final_stocks]

    def save_model(self, request, obj, form, change):
        obj.user_id = request.user
        super().save_model(request, obj, form, change)


# KITCHEN CRUD
@admin.register(Kitchen)
class KitchenAdmin(admin.ModelAdmin):
    exclude = ("user_id",)
    list_display = ("name", "food_category")
    list_filter = ("food_category",)
    ordering = ("name",)
    search_fields = ("name",)
    actions = [make_kitchen_initial_stocks, make_kitchen_final_stocks]

    def save_model(self, request, obj, form, change):
        obj.user_id = request.user
        super().save_model(request, obj, form, change)


# MISCELLANEOUS CRUD
@admin.register(Miscellaneous)
class MiscellaneousAdmin(admin.ModelAdmin):
    exclude = ("user_id",)
    list_display = ("name", "price_unit_dollar",)
    list_display_links = ("name", "price_unit_dollar")
    ordering = ("name",)
    search_fields = ("name",)

    def save_model(self, request, obj, form, change):
        obj.user_id = request.user
        super().save_model(request, obj, form, change)

#################################################################################


# STOCK INVENTORY
@admin.register(Stock)
class InitialStockAdmin(admin.ModelAdmin):
    exclude = ("created_at", "updated_at")
    list_display = ("bar_initial_id", "bar_final_id", "goodies_initial_id", "goodies_final_id",
                    "kitchen_initial_id", "kitchen_final_id", "trip_id", "quantity")
    ordering = ("trip_id",)
    search_fields = ("trip_id",)
    list_filter = ("trip_id",)
