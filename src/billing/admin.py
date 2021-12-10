# -*- coding: utf-8 -*-
# pylint: disable=missing-class-docstring
"""All the admin pages to create, update, delete and read the order lines, \
    the bills and the payments.
    """
from django.contrib import admin
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Bill, OrderLine, Payment


# CUSTOM ADMIN ACTION TO MAKE THE BILL WITH THE ORDER LINE(S) SELECTED.
@admin.action(description='Faire la facture des commandes sélectionnées')
def make_bill(modeladmin, request, queryset):
    """ Action pour faire la facture des commandes sélectionnées ; \
        envoi vers une page intermédiaire ; enregistrement des données \
        dans la table de Bill."""
    print("TTTTTTTTT : ", request.POST)
    if "apply" in request.POST:
        # Saving the data from the order line(s) form of a guest
        # to create an instance in the Bill table with those data.
        print("XXXXXXXXXXX : ", request.POST)
        orderline_list = request.POST.getlist('_selected_action')
        email_selected = request.POST['email']
        # trip_id_selected = Trip.objects.filter(id=trip_selected).last()
        # i = 0
        for orderline in orderline_list:
            orderline_selected = OrderLine.objects.filter(id=orderline).last()

        #     if drink_quantity_list[i]:
        #         drink_quantity = drink_quantity_list[i]
        #     else:
        #         drink_quantity = 0
        #     i = i + 1
        #     if drink_quantity != 0:
        #         drink_id_selected = Bar.objects.filter(id=drink).last()
        #         bar_initial_item = Stock(bar_initial_id=drink_id_selected,
        #                                  trip_id=trip_id_selected, quantity=drink_quantity,
        #                                  user_id=request.user)
        #         bar_initial_item.save()
        # return HttpResponseRedirect('/admin')

    # To display the stock inventory with all the drinks registered into the database
    # with the choice of trips.
    else:
        all_orderlines = queryset.all()

    # What to render to the template.
    all_orderlines = queryset.all()
    print("IIIIIIII : ", all_orderlines[0].guest_id.trips)
    return render(request, 'admin/bill.html',
                  context={"orderlines": all_orderlines})


#################################################################################


# ORDERLINE CRUD
@admin.register(OrderLine)
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
@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    exclude = ("user_id", "date", "amount")
    # show a button to click that leads to a bill form.  TODO

    def save_model(self, request, obj, form, change):
        obj.user_id = request.user
        super().save_model(request, obj, form, change)


# PAYMENT CRUD
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    exclude = ("user_id", "date")
    list_filter = ("payment_mode",)
    ordering = ("payment_mode",)
    search_fields = ("payment_mode",)

    def save_model(self, request, obj, form, change):
        obj.user_id = request.user
        super().save_model(request, obj, form, change)
