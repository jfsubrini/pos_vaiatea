# -*- coding: utf-8 -*-
# pylint: disable=missing-class-docstring
"""All the admin pages to create, update, delete and read \
    all the bar, kitchen, goodies and miscellanous items.
    Idem for the initial and final stocks of the bar, kitchen \
        and goodies items.
    """
from django.contrib import admin
from stocks.forms import BarStockForm, KitchenStockForm, GoodiesStockForm
from stocks.models import (
    Bar,
    Goodies,
    Kitchen,
    Miscellaneous,
    Stock
)

# from django.core import serializers
# from django.http import HttpResponse


# BAR
@admin.action(description='Relevé du stock initial du bar')
def make_bar_initial_stocks(modeladmin, request, queryset):
    """ select Relevé du stock initial du bar puis envoyer arrivée sur une page \
        où on va demander le trip et on va afficher toutes les boissons \
            avec un formulaire pour mettre les quantités."""
    # for item in range(queryset.count()):
    # for item in queryset:
    #     # item_bar_id = queryset.values_list('id', flat=True)[0]
    #     item_bar_id = item.id
    #     bar_initial = Stock(
    #         bar_initial_id=item_bar_id, trip_id=1, quantity=1)
    #     bar_initial.save()

    # response = HttpResponse(content_type="application/json")
    # serializers.serialize("json", queryset, stream=response)
    # return response


@admin.action(description='Relevé du stock final du bar')
def make_bar_final_stocks(modeladmin, request, queryset):
    # queryset.update(status='p')
    pass


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


# GOODIES
# @admin.action(description='Relevé du stock initial des goodies')
# def make_goodies_initial_stocks(modeladmin, request, queryset):
#     # queryset.update(status='p')
#     pass


# @admin.action(description='Relevé du stock final des goodies')
# def make_goodies_final_stocks(modeladmin, request, queryset):
#     # queryset.update(status='p')
#     pass


@admin.register(Goodies)
class GoodiesAdmin(admin.ModelAdmin):
    exclude = ("user_id",)
    list_display = ("name", "price_unit_dollar",
                    "goodies_category", "size", "color", "gender")
    list_display_links = ("name", "price_unit_dollar")
    list_filter = ("goodies_category", "size")
    ordering = ("name",)
    search_fields = ("name",)
    # actions = [make_goodies_initial_stocks, make_goodies_final_stocks]

    def save_model(self, request, obj, form, change):
        obj.user_id = request.user
        super().save_model(request, obj, form, change)


# KITCHEN
# @admin.action(description='Relevé du stock initial en cuisine')
# def make_kitchen_initial_stocks(modeladmin, request, queryset):
#     # queryset.update(status='p')
#     pass


# @admin.action(description='Relevé du stock final en cuisine')
# def make_kitchen_final_stocks(modeladmin, request, queryset):
#     # queryset.update(status='p')
#     pass


@admin.register(Kitchen)
class KitchenAdmin(admin.ModelAdmin):
    exclude = ("user_id",)
    list_display = ("name", "food_category")
    list_filter = ("food_category",)
    ordering = ("name",)
    search_fields = ("name",)
    # actions = [make_kitchen_initial_stocks, make_kitchen_final_stocks]

    def save_model(self, request, obj, form, change):
        obj.user_id = request.user
        super().save_model(request, obj, form, change)


# MISCELLANEOUS
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


# STOCK BAR
@admin.action(description='Inventaire du stock initial du bar')
def make_bar_initial_stocks(modeladmin, request, queryset):
    # Envoyer vers une page intermediaire avec liste de tous les items et le moyen de mettre la quantité. TODO
    pass


@admin.action(description='Inventaire du stock final du bar')
def make_bar_final_stocks(modeladmin, request, queryset):
    # Envoyer vers une page intermediaire avec liste de tous les items et le moyen de mettre la quantité. TODO
    pass


class StockBarAdmin(admin.AdminSite):
    site_header = 'Vaiatea Stock Administration'
    site_title = 'Relevé de stock du bar'
    index_title = 'Relevé de stock du bar'

    def save_model(self, request, obj, form, change):
        obj.user_id = request.user
        super().save_model(request, obj, form, change)


admin_bar_stock = StockBarAdmin(name='stockbaradmin')


@admin.register(Bar, site=admin_bar_stock)
class BarStockAdmin(admin.ModelAdmin):
    form = BarStockForm  #  Marche pas TODO
    fields = ("trip_id",)  #  Marche pas TODO
    actions = [make_bar_initial_stocks, make_bar_final_stocks]


# STOCK KITCHEN
@admin.action(description='Inventaire du stock initial de la cuisine')
def make_kitchen_initial_stocks(modeladmin, request, queryset):
    # Envoyer vers une page intermediaire avec liste de tous les items et le moyen de mettre la quantité. TODO
    pass


@admin.action(description='Inventaire du stock final de la cuisine')
def make_kitchen_final_stocks(modeladmin, request, queryset):
    # Envoyer vers une page intermediaire avec liste de tous les items et le moyen de mettre la quantité. TODO
    pass


class StockKitchenAdmin(admin.AdminSite):
    site_header = 'Vaiatea Stock Administration'
    site_title = 'Relevé de stock de la cuisine'
    index_title = 'Relevé de stock de la cuisine'

    def save_model(self, request, obj, form, change):
        obj.user_id = request.user
        super().save_model(request, obj, form, change)


admin_kitchen_stock = StockKitchenAdmin(name='stockkitchenadmin')


@admin.register(Kitchen, site=admin_kitchen_stock)
class KitchenStockAdmin(admin.ModelAdmin):
    form = KitchenStockForm  #  Marche pas TODO
    fields = ("trip_id",)  #  Marche pas TODO
    actions = [make_kitchen_initial_stocks, make_kitchen_final_stocks]


# STOCK GOODIES
@admin.action(description='Inventaire du stock initial des goodies')
def make_goodies_initial_stocks(modeladmin, request, queryset):
    # Envoyer vers une page intermediaire avec liste de tous les items et le moyen de mettre la quantité. TODO
    pass


@admin.action(description='Inventaire du stock final des goodies')
def make_goodies_final_stocks(modeladmin, request, queryset):
    # Envoyer vers une page intermediaire avec liste de tous les items et le moyen de mettre la quantité. TODO
    pass


class StockGoodiesAdmin(admin.AdminSite):
    site_header = 'Vaiatea Stock Administration'
    site_title = 'Relevé de stock des goodies'
    index_title = 'Relevé de stock des goodies'

    def save_model(self, request, obj, form, change):
        obj.user_id = request.user
        super().save_model(request, obj, form, change)


admin_goodies_stock = StockGoodiesAdmin(name='stockgoodiesadmin')


@admin.register(Goodies, site=admin_goodies_stock)
class GoodiesStockAdmin(admin.ModelAdmin):
    form = GoodiesStockForm  #  Marche pas TODO
    fields = ("trip_id",)  #  Marche pas TODO
    actions = [make_goodies_initial_stocks, make_goodies_final_stocks]
