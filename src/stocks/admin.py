# -*- coding: utf-8 -*-
# pylint: disable=missing-class-docstring, no-member, invalid-name
"""All the admin pages to create, update, delete and read \
    all the bar, kitchen, goodies and miscellanous items.
    Idem for the initial and final stocks inventory of the bar, \
        kitchen and goodies items.
    """
from django.contrib import admin
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import (
    Trip,
    Bar,
    Goodies,
    Kitchen,
    Miscellaneous,
    Stock,
    InitialBarStock,
    FinalBarStock,
    InitialKitchenStock,
    FinalKitchenStock,
    InitialGoodiesStock,
    FinalGoodiesStock,
)


# CUSTOM ADMIN ACTIONS TO CREATE INITIAL AND FINAL STOCKS INVENTORIES.
# Initial Bar Stock inventory action from the Bar list page.
@admin.action(description='Inventaire du stock initial du bar')
def make_bar_initial_stocks(modeladmin, request, queryset):
    """ Action pour faire un inventaire du stock initial du bar ; \
        envoi vers une page intermédiaire ; enregistrement des données \
        dans la table de Stock."""
    if "apply" in request.POST:
        # Saving the data from the initial bar stock inventory form
        # to update the Stock table with those data.
        drinks_list = request.POST.getlist('_selected_action')
        drink_quantity_list = request.POST.getlist('drink_quantity')
        trip_selected = request.POST['trip']
        trip_id_selected = Trip.objects.filter(id=trip_selected).last()
        i = 0
        for drink in drinks_list:
            if drink_quantity_list[i]:
                drink_quantity = drink_quantity_list[i]
            else:
                drink_quantity = 0
            i = i + 1
            if drink_quantity != 0:
                drink_id_selected = Bar.objects.filter(id=drink).last()
                bar_initial_item = Stock(bar_initial_id=drink_id_selected,
                                         trip_id=trip_id_selected, quantity=drink_quantity,
                                         user_id=request.user)
                bar_initial_item.save()
        return HttpResponseRedirect('/admin')

    # To display the stock inventory with all the drinks registered into the database
    # with the choice of trips.
    else:
        all_drinks = queryset.all()
        all_trips = Trip.objects.all()

    # What to render to the template.
    all_drinks = queryset.all()
    all_trips = Trip.objects.all()
    return render(request, 'admin/bar_initial_stocks.html',
                  context={"drinks": all_drinks, "trips": all_trips})


# Final Bar Stock inventory action from the Bar list page.
@ admin.action(description='Inventaire du stock final du bar')
def make_bar_final_stocks(modeladmin, request, queryset):
    """ Action pour faire un inventaire du stock final du bar ; \
        envoi vers une page intermédiaire ; enregistrement des données \
        dans la table de Stock."""
    if "apply" in request.POST:
        # Saving the data from the final bar stock inventory form
        # to update the Stock table with those data.
        drinks_list = request.POST.getlist('_selected_action')
        drink_quantity_list = request.POST.getlist('drink_quantity')
        trip_selected = request.POST['trip']
        trip_id_selected = Trip.objects.filter(id=trip_selected).last()
        i = 0
        for drink in drinks_list:
            if drink_quantity_list[i]:
                drink_quantity = drink_quantity_list[i]
            else:
                drink_quantity = 0
            i = i + 1
            drink_id_selected = Bar.objects.filter(id=drink).last()
            bar_final_item = Stock(bar_final_id=drink_id_selected,
                                   trip_id=trip_id_selected, quantity=drink_quantity,
                                   user_id=request.user)
            bar_final_item.save()
        return HttpResponseRedirect('/admin')

    # To display the stock inventory with all the drinks registered into the database
    # with the choice of trips.
    else:
        all_drinks = queryset.all()
        all_trips = Trip.objects.all()

    # What to render to the template.
    all_drinks = queryset.all()
    all_trips = Trip.objects.all()
    return render(request, 'admin/bar_final_stocks.html',
                  context={"drinks": all_drinks, "trips": all_trips})


# Initial Goodies Stock inventory action from the Goodies list page.
@ admin.action(description='Inventaire du stock initial des goodies')
def make_goodies_initial_stocks(modeladmin, request, queryset):
    """ Action pour faire un inventaire du stock initial de goodies ; \
        envoi vers une page intermédiaire ; enregistrement des données \
        dans la table de Stock."""
    if "apply" in request.POST:
        # Saving the data from the initial goodies stock inventory form
        # to update the Stock table with those data.
        goodies_list = request.POST.getlist('_selected_action')
        goody_quantity_list = request.POST.getlist('goody_quantity')
        trip_selected = request.POST['trip']
        trip_id_selected = Trip.objects.filter(id=trip_selected).last()
        i = 0
        for goody in goodies_list:
            if goody_quantity_list[i]:
                goody_quantity = goody_quantity_list[i]
            else:
                goody_quantity = 0
            i = i + 1
            if goody_quantity != 0:
                goody_id_selected = Goodies.objects.filter(id=goody).last()
                goodies_initial_item = Stock(goodies_initial_id=goody_id_selected,
                                             trip_id=trip_id_selected, quantity=goody_quantity,
                                             user_id=request.user)
                goodies_initial_item.save()
        return HttpResponseRedirect('/admin')

    # To display the stock inventory with all the goodies registered into the database
    # with the choice of trips.
    else:
        all_goodies = queryset.all()
        all_trips = Trip.objects.all()

    # What to render to the template.
    all_goodies = queryset.all()
    all_trips = Trip.objects.all()
    return render(request, 'admin/goodies_initial_stocks.html',
                  context={"goodies": all_goodies, "trips": all_trips})


# Final Goodies Stock inventory action from the Goodies list page.
@ admin.action(description='Inventaire du stock final des goodies')
def make_goodies_final_stocks(modeladmin, request, queryset):
    """ Action pour faire un inventaire du stock final de goodies ; \
        envoi vers une page intermédiaire ; enregistrement des données \
        dans la table de Stock."""
    if "apply" in request.POST:
        # Saving the data from the final goodies stock inventory form
        # to update the Stock table with those data.
        goodies_list = request.POST.getlist('_selected_action')
        goody_quantity_list = request.POST.getlist('goody_quantity')
        trip_selected = request.POST['trip']
        trip_id_selected = Trip.objects.filter(id=trip_selected).last()
        i = 0
        for goody in goodies_list:
            if goody_quantity_list[i]:
                goody_quantity = goody_quantity_list[i]
            else:
                goody_quantity = 0
            i = i + 1
            goody_id_selected = Goodies.objects.filter(id=goody).last()
            goodies_final_item = Stock(goodies_final_id=goody_id_selected,
                                       trip_id=trip_id_selected, quantity=goody_quantity,
                                       user_id=request.user)
            goodies_final_item.save()
        return HttpResponseRedirect('/admin')

    # To display the stock inventory with all the goodies registered into the database
    # with the choice of trips.
    else:
        all_goodies = queryset.all()
        all_trips = Trip.objects.all()

    # What to render to the template.
    all_goodies = queryset.all()
    all_trips = Trip.objects.all()
    return render(request, 'admin/goodies_final_stocks.html',
                  context={"goodies": all_goodies, "trips": all_trips})


# Initial Kitchen Stock inventory action from the Kitchen list page.
@ admin.action(description='Inventaire du stock initial en cuisine')
def make_kitchen_initial_stocks(modeladmin, request, queryset):
    """ Action pour faire un inventaire du stock initial de la cuisine ; \
        envoi vers une page intermédiaire ; enregistrement des données \
        dans la table de Stock."""
    if "apply" in request.POST:
        # Saving the data from the initial kitchen stock inventory form
        # to update the Stock table with those data.
        foods_list = request.POST.getlist('_selected_action')
        food_quantity_list = request.POST.getlist('food_quantity')
        trip_selected = request.POST['trip']
        trip_id_selected = Trip.objects.filter(id=trip_selected).last()
        i = 0
        for food in foods_list:
            if food_quantity_list[i]:
                food_quantity = food_quantity_list[i]
            else:
                food_quantity = 0
            i = i + 1
            if food_quantity != 0:
                food_id_selected = Kitchen.objects.filter(id=food).last()
                kitchen_initial_item = Stock(kitchen_initial_id=food_id_selected,
                                             trip_id=trip_id_selected, quantity=food_quantity,
                                             user_id=request.user)
                kitchen_initial_item.save()
        return HttpResponseRedirect('/admin')

    # To display the stock inventory with all the foods registered into the database
    # with the choice of trips.
    else:
        all_food = queryset.all()
        all_trips = Trip.objects.all()

    # What to render to the template.
    all_food = queryset.all()
    all_trips = Trip.objects.all()
    return render(request, 'admin/kitchen_initial_stocks.html',
                  context={"foods": all_food, "trips": all_trips})


# Final Kitchen Stock inventory action from the Kitchen list page.
@ admin.action(description='Inventaire du stock final en cuisine')
def make_kitchen_final_stocks(modeladmin, request, queryset):
    """ Action pour faire un inventaire du stock final de la cuisine ; \
        envoi vers une page intermédiaire ; enregistrement des données \
        dans la table de Stock."""
    if "apply" in request.POST:
        # Saving the data from the final kitchen stock inventory form
        # to update the Stock table with those data.
        foods_list = request.POST.getlist('_selected_action')
        food_quantity_list = request.POST.getlist('food_quantity')
        trip_selected = request.POST['trip']
        trip_id_selected = Trip.objects.filter(id=trip_selected).last()
        i = 0
        for food in foods_list:
            if food_quantity_list[i]:
                food_quantity = food_quantity_list[i]
            else:
                food_quantity = 0
            i = i + 1
            food_id_selected = Kitchen.objects.filter(id=food).last()
            kitchen_final_item = Stock(kitchen_final_id=food_id_selected,
                                       trip_id=trip_id_selected, quantity=food_quantity,
                                       user_id=request.user)
            kitchen_final_item.save()
        return HttpResponseRedirect('/admin')

    # To display the stock inventory with all the foods registered into the database
    # with the choice of trips.
    else:
        all_food = queryset.all()
        all_trips = Trip.objects.all()

    # What to render to the template.
    all_food = queryset.all()
    all_trips = Trip.objects.all()
    return render(request, 'admin/kitchen_final_stocks.html',
                  context={"foods": all_food, "trips": all_trips})

#################################################################################


# BAR CRUD
@ admin.register(Bar)
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
@ admin.register(Goodies)
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
@ admin.register(Kitchen)
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
@ admin.register(Miscellaneous)
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


# STOCK INVENTORY LISTS AND UPDATE
@ admin.register(InitialBarStock)
class InitialBarStockAdmin(admin.ModelAdmin):
    exclude = ("user_id", "bar_final_id", "kitchen_initial_id", "kitchen_final_id",
               "goodies_initial_id", "goodies_final_id")
    list_display = ("bar_initial_id", "quantity", "trip_id")
    ordering = ("trip_id",)
    list_filter = ("trip_id", "bar_initial_id")

    def get_queryset(self, request):
        item_queryset = super().get_queryset(request)
        return item_queryset.filter(bar_initial_id__gt=0)


@ admin.register(FinalBarStock)
class FinalBarStockAdmin(admin.ModelAdmin):
    exclude = ("user_id", "bar_initial_id", "kitchen_initial_id", "kitchen_final_id",
               "goodies_initial_id", "goodies_final_id")
    list_display = ("bar_final_id", "quantity", "trip_id")
    ordering = ("trip_id",)
    list_filter = ("trip_id", "bar_final_id")

    def get_queryset(self, request):
        item_queryset = super().get_queryset(request)
        return item_queryset.filter(bar_final_id__gt=0)


@ admin.register(InitialKitchenStock)
class InitialKitchenStockAdmin(admin.ModelAdmin):
    exclude = ("user_id", "bar_initial_id", "bar_final_id", "kitchen_final_id",
               "goodies_initial_id", "goodies_final_id")
    list_display = ("kitchen_initial_id", "quantity", "trip_id")
    ordering = ("trip_id",)
    list_filter = ("trip_id", "kitchen_initial_id")

    def get_queryset(self, request):
        item_queryset = super().get_queryset(request)
        return item_queryset.filter(kitchen_initial_id__gt=0)


@ admin.register(FinalKitchenStock)
class FinalKitchenStockAdmin(admin.ModelAdmin):
    exclude = ("user_id", "bar_initial_id", "bar_final_id", "kitchen_initial_id",
               "goodies_initial_id", "goodies_final_id")
    list_display = ("kitchen_final_id", "quantity", "trip_id")
    ordering = ("trip_id",)
    list_filter = ("trip_id", "kitchen_final_id")

    def get_queryset(self, request):
        item_queryset = super().get_queryset(request)
        return item_queryset.filter(kitchen_final_id__gt=0)


@ admin.register(InitialGoodiesStock)
class InitialGoodiesStockAdmin(admin.ModelAdmin):
    exclude = ("user_id", "bar_initial_id", "bar_final_id", "kitchen_initial_id",
               "kitchen_final_id", "goodies_final_id")
    list_display = ("goodies_initial_id", "quantity", "trip_id")
    ordering = ("trip_id",)
    list_filter = ("trip_id", "goodies_initial_id")

    def get_queryset(self, request):
        item_queryset = super().get_queryset(request)
        return item_queryset.filter(goodies_initial_id__gt=0)


@ admin.register(FinalGoodiesStock)
class FinalGoodiesStockAdmin(admin.ModelAdmin):
    exclude = ("user_id", "bar_initial_id", "bar_final_id", "kitchen_initial_id",
               "kitchen_final_id", "goodies_initial_id")
    list_display = ("goodies_final_id", "quantity", "trip_id")
    ordering = ("trip_id",)
    list_filter = ("trip_id", "goodies_final_id")

    def get_queryset(self, request):
        item_queryset = super().get_queryset(request)
        return item_queryset.filter(goodies_final_id__gt=0)
