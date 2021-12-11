# -*- coding: utf-8 -*-
# pylint: disable=missing-class-docstring
"""All the admin pages to create, update, delete and read the order lines, \
    the bills and the payments.
    """
from types import prepare_class
from typing import ParamSpecArgs
from django.contrib import admin
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import (
    Bar,
    Bill,
    Goodies,
    Miscellaneous,
    OrderLine,
    Payment,
)


# Function to calculate the amount of each order line.
def amounts_calculation(all_orderlines_qs):
    """Calculation of the amount for each order line of the bill."""
    amounts_list = []
    for orderline in all_orderlines_qs:
        quantity_item = orderline.quantity
        if orderline.bar_id:
            bar_selected = Bar.objects.filter(orderlines=orderline.id)
            unit_price_item = bar_selected[0].price_unit_dollar
        elif orderline.goodies_id:
            goody_selected = Goodies.objects.filter(orderlines=orderline.id)
            unit_price_item = goody_selected[0].price_unit_dollar
        elif orderline.miscellaneous_id:
            misc_selected = Miscellaneous.objects.filter(
                orderlines=orderline.id)
            unit_price_item = misc_selected[0].price_unit_dollar
        orderline_amount = float(quantity_item * unit_price_item)
        amounts_list.append(orderline_amount)
    return amounts_list


# Function to send the bill by email.
def send_email(email):
    pass


# CUSTOM ADMIN ACTION TO MAKE THE BILL WITH THE ORDER LINE(S) SELECTED.
@ admin.action(description='Faire la facture des commandes sélectionnées')
def make_bill(modeladmin, request, queryset):
    """ Action pour faire la facture des commandes sélectionnées ; \
        envoi vers une page intermédiaire ; enregistrement des données \
        dans la table de Bill."""
    # Send the order lines data and the guest's email to display in the bill template.
    # Calculation of the amount for each order line and the total amount of the bill.
    all_orderlines = queryset.all()
    all_amounts = amounts_calculation(all_orderlines)
    total_amount = sum(all_amounts)
    zipped_data = zip(all_orderlines, all_amounts)
    email_selected = all_orderlines[0].guest_id.email
    print("DEHORS : ", request.POST)  # TODO
    if "apply" in request.POST:  # Je n'arrive pas à entrer là-dedans
        # Saving the data from the order line(s) form of a guest
        # to create an instance in the Bill table with those data.
        print("DEDANS : ", request.POST)  #  TODO
        orderline_list = request.POST.getlist('_selected_action')
        # Create the bill instance with the total amount to pay and tha user_id
        new_bill = Bill(user_id=request.user, amount=total_amount)
        new_bill.save()
        # Mettre l'id du bill créé dans tous les order lines auquel il se réfère.
        for orderline in orderline_list:
            orderline_selected = OrderLine.objects.filter(id=orderline).last()
            orderline_selected.bill_id = new_bill.id
            orderline_selected.save()
        # Envoi ou non de la facture par email.
        email_check = request.POST.getlist('email_checkbox')
        if email_check:
            send_email(email_selected)
        return HttpResponseRedirect('/admin')

    # What to render to the template.
    return render(request, 'admin/bill.html',
                  context={"orderlines": all_orderlines,
                           "zipped_data": zipped_data,
                           "total_amount": total_amount,
                           "email": email_selected})


#################################################################################


# ORDERLINE CRUD
@ admin.register(OrderLine)
class OrderLineAdmin(admin.ModelAdmin):
    # Si choix de differente categorie d'article raise error : une ligne a la fois  TODO
    exclude = ("user_id", "date", "bill_id")
    list_display = ("guest_id",  "quantity", "bar_id", "goodies_id",
                    "miscellaneous_id")
    list_filter = ("guest_id",)
    ordering = ("guest_id",)
    search_fields = ("guest_id", "bar_id", "goodies_id", "miscellaneous_id")
    actions = [make_bill]

    def save_model(self, request, obj, form, change):
        obj.user_id = request.user
        super().save_model(request, obj, form, change)


# BILL CRUD
@ admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    exclude = ("user_id", "date", "amount")
    # show a button to click that leads to a bill form.  TODO

    def save_model(self, request, obj, form, change):
        obj.user_id = request.user
        super().save_model(request, obj, form, change)


# PAYMENT CRUD
@ admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    exclude = ("user_id", "date")
    list_filter = ("payment_mode",)
    ordering = ("payment_mode",)
    search_fields = ("payment_mode",)

    def save_model(self, request, obj, form, change):
        obj.user_id = request.user
        super().save_model(request, obj, form, change)
