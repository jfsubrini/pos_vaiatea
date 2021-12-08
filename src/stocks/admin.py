# -*- coding: utf-8 -*-
# pylint: disable=missing-class-docstring
"""All the admin pages to create, update, delete and read \
    all the bar, kitchen, goodies and miscellanous items.
    Idem for the initial and final stocks inventory of the bar, \
        kitchen and goodies items.
    """
from django.contrib import admin
from django.contrib.admin import AdminSite
from django.shortcuts import render
# from stocks.forms import BarStockForm, KitchenStockForm, GoodiesStockForm
from stocks.models import (
    Bar,
    Goodies,
    Kitchen,
    Miscellaneous,
    Stock
)
from .forms import QuantityForm


# Custom Admin page
# class StockBarAdmin(admin.AdminSite):
#     site_header = 'Vaiatea Stock Administration'
#     site_title = 'Relevé de stock du bar'
#     index_title = 'Relevé de stock du bar'


# admin_site = StockBarAdmin(name=baradmin)

# @admin.register(Bar, site=admin_site)


#################################################################################
# Actions in the items' lists to make initial and final inventory of the items.
@admin.action(description='Inventaire du stock initial du bar')
def make_bar_initial_stocks(modeladmin, request, queryset):
    """ Choix dans action pour faire un inventaire du stock initial du bar \
        puis envoi vers une page intermédiaire."""
    # Ceci dessous servira plus tard à enregistrer les items dans les stocks. Testé en attendant.
    # for item in range(queryset.count()):
    # for item in queryset:
    #     print("XXXXXXXXX : ", item.id, type(item.id))
    #     bar_initial = Stock(
    #         bar_initial_id=item.id, trip_id=1, quantity=1)
    #     bar_initial.save()
    # if "apply" in request.POST:
    all_drinks = queryset.all()
    quantity_form = QuantityForm()
    return render(request, 'admin/bar_initial_stocks.html',
                  context={"drinks": all_drinks, "quantity_form": quantity_form})


@admin.action(description='Inventaire du stock final du bar')
def make_bar_final_stocks(modeladmin, request, queryset):
    """ Choix dans action pour faire un inventaire du stock final du bar \
        puis envoi vers une page intermédiaire."""
    all_drinks = queryset.all()
    quantity_form = QuantityForm()
    return render(request, 'admin/bar_final_stocks.html',
                  context={"drinks": all_drinks, "quantity_form": quantity_form})


@admin.action(description='Inventaire du stock initial des goodies')
def make_goodies_initial_stocks(modeladmin, request, queryset):
    """ Choix dans action pour faire un inventaire du stock initial des goodies \
        puis envoi vers une page intermédiaire."""
    all_goodies = queryset.all()
    quantity_form = QuantityForm()
    return render(request, 'admin/goodies_initial_stocks.html',
                  context={"goodies": all_goodies, "quantity_form": quantity_form})


@admin.action(description='Inventaire du stock final des goodies')
def make_goodies_final_stocks(modeladmin, request, queryset):
    """ Choix dans action pour faire un inventaire du stock final des goodies \
        puis envoi vers une page intermédiaire."""
    all_goodies = queryset.all()
    quantity_form = QuantityForm()
    return render(request, 'admin/goodies_final_stocks.html',
                  context={"goodies": all_goodies, "quantity_form": quantity_form})


@admin.action(description='Inventaire du stock initial en cuisine')
def make_kitchen_initial_stocks(modeladmin, request, queryset):
    """ Choix dans action pour faire un inventaire du stock initial en cuisine \
        puis envoi vers une page intermédiaire."""
    all_food = queryset.all()
    quantity_form = QuantityForm()
    return render(request, 'admin/kitchen_initial_stocks.html',
                  context={"foods": all_food, "quantity_form": quantity_form})


@admin.action(description='Inventaire du stock final en cuisine')
def make_kitchen_final_stocks(modeladmin, request, queryset):
    """ Choix dans action pour faire un inventaire du stock final en cuisine \
        puis envoi vers une page intermédiaire."""
    all_food = queryset.all()
    quantity_form = QuantityForm()
    return render(request, 'admin/kitchen_final_stocks.html',
                  context={"foods": all_food, "quantity_form": quantity_form})

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
# STOCK BAR
# @admin.action(description='Relevé du stock initial du bar')
# def make_bar_initial_stocks(modeladmin, request, queryset):
#     """ select Relevé du stock initial du bar puis envoyer arrivée sur une page \
#         où on va demander le trip et on va afficher toutes les boissons \
#             avec un formulaire pour mettre les quantités."""
#     # A TESTER, apres il faudra trouver le trip_id et la quantity :
#     for item in range(queryset.count()):
#         item_bar_id = queryset[item].id
#         bar_initial = Stock(
#             bar_initial_id=item_bar_id, trip_id=1, quantity=1)
#         bar_initial.save()


# @admin.action(description='Inventaire du stock initial du bar')
# def make_bar_initial_stocks(modeladmin, request, queryset):
#     # Envoyer vers une page intermediaire avec liste de tous les items et le moyen de mettre la quantité. TODO
#     pass


# @admin.action(description='Inventaire du stock final du bar')
# def make_bar_final_stocks(modeladmin, request, queryset):
#     # Envoyer vers une page intermediaire avec liste de tous les items et le moyen de mettre la quantité. TODO
#     pass


# class StockBarAdmin(admin.AdminSite):
#     site_header = 'Vaiatea Stock Administration'
#     site_title = 'Relevé de stock du bar'
#     index_title = 'Relevé de stock du bar'

#     def save_model(self, request, obj, form, change):
#         obj.user_id = request.user
#         super().save_model(request, obj, form, change)


# admin_bar_stock = StockBarAdmin(name='stockbaradmin')


# @admin.register(Bar, site=admin_bar_stock)
# class BarStockAdmin(admin.ModelAdmin):
#     form = BarStockForm  #  Marche pas TODO
#     fields = ("trip_id",)  #  Marche pas TODO
#     actions = [make_bar_initial_stocks, make_bar_final_stocks]


# # STOCK KITCHEN
# @admin.action(description='Inventaire du stock initial de la cuisine')
# def make_kitchen_initial_stocks(modeladmin, request, queryset):
#     # Envoyer vers une page intermediaire avec liste de tous les items et le moyen de mettre la quantité. TODO
#     pass


# @admin.action(description='Inventaire du stock final de la cuisine')
# def make_kitchen_final_stocks(modeladmin, request, queryset):
#     # Envoyer vers une page intermediaire avec liste de tous les items et le moyen de mettre la quantité. TODO
#     pass


# class StockKitchenAdmin(admin.AdminSite):
#     site_header = 'Vaiatea Stock Administration'
#     site_title = 'Relevé de stock de la cuisine'
#     index_title = 'Relevé de stock de la cuisine'

#     def save_model(self, request, obj, form, change):
#         obj.user_id = request.user
#         super().save_model(request, obj, form, change)


# admin_kitchen_stock = StockKitchenAdmin(name='stockkitchenadmin')


# @admin.register(Kitchen, site=admin_kitchen_stock)
# class KitchenStockAdmin(admin.ModelAdmin):
#     form = KitchenStockForm  #  Marche pas TODO
#     fields = ("trip_id",)  #  Marche pas TODO
#     actions = [make_kitchen_initial_stocks, make_kitchen_final_stocks]


# # STOCK GOODIES
# @admin.action(description='Inventaire du stock initial des goodies')
# def make_goodies_initial_stocks(modeladmin, request, queryset):
#     # Envoyer vers une page intermediaire avec liste de tous les items et le moyen de mettre la quantité. TODO
#     pass


# @admin.action(description='Inventaire du stock final des goodies')
# def make_goodies_final_stocks(modeladmin, request, queryset):
#     # Envoyer vers une page intermediaire avec liste de tous les items et le moyen de mettre la quantité. TODO
#     pass


# class StockGoodiesAdmin(admin.AdminSite):
#     site_header = 'Vaiatea Stock Administration'
#     site_title = 'Relevé de stock des goodies'
#     index_title = 'Relevé de stock des goodies'

#     def save_model(self, request, obj, form, change):
#         obj.user_id = request.user
#         super().save_model(request, obj, form, change)


# admin_goodies_stock = StockGoodiesAdmin(name='stockgoodiesadmin')


# @admin.register(Goodies, site=admin_goodies_stock)
# class GoodiesStockAdmin(admin.ModelAdmin):
#     form = GoodiesStockForm  #  Marche pas TODO
#     fields = ("trip_id",)  #  Marche pas TODO
#     actions = [make_goodies_initial_stocks, make_goodies_final_stocks]
