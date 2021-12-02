# -*- coding: utf-8 -*-
# pylint: disable=missing-class-docstring
"""All the admin pages to create, update, delete and read the order lines, \
    the bills and the payments.
    """
from django.contrib import admin
from .models import Bill, OrderLine, Payment


@admin.register(OrderLine)
class OrderLineAdmin(admin.ModelAdmin):
    exclude = ("user_id", "date", "bill_id")
    list_display = ("guest_id", "bar_id", "goodies_id",
                    "miscellaneous_id", "quantity")
    list_filter = ("guest_id",)
    ordering = ("guest_id",)
    search_fields = ("guest_id", "bar_id", "goodies_id", "miscellaneous_id")
    # Si choix de differente categorie d'article raise error : une ligne a la fois

    def save_model(self, request, obj, form, change):
        obj.user_id = request.user
        super().save_model(request, obj, form, change)


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    exclude = ("user_id", "date", "amount")
    # show a button to click that leads to a bill form.  TODO

    def save_model(self, request, obj, form, change):
        obj.user_id = request.user
        super().save_model(request, obj, form, change)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    exclude = ("user_id", "date")
    list_filter = ("payment_mode",)
    ordering = ("payment_mode",)
    search_fields = ("payment_mode",)

    def save_model(self, request, obj, form, change):
        obj.user_id = request.user
        super().save_model(request, obj, form, change)
