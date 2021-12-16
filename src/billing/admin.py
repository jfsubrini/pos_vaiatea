# -*- coding: utf-8 -*-
# pylint: disable=missing-class-docstring, no-member
"""All the admin pages to create, update, delete and read the order lines, \
    the bills and the payments.
    """
from django.contrib import admin
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import (
    Bar,
    Bill,
    BillPaid,
    Goodies,
    InvoicedOrder,
    Miscellaneous,
    OrderLine,
    Payment,
)
from .forms import OrderLineForm, PaymentForm
from .emailing import send_email


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


# CUSTOM ADMIN ACTIONS TO MAKE THE BILL AND THE PAYMENT.
# Billing action to make the bill with the order line(s) selected from one guest.
@ admin.action(description='Faire la facture des commandes sélectionnées')
def make_bill(modeladmin, request, queryset):
    """ Admin Action to make the bill with the selected order line(s); \
        sending to an intermediate page to display the data ; saving the data \
        into the Bill and OrderLine tables. Sending the bill by email."""
    # Calculation of the amount for each order line and the total amount of the bill.
    all_orderlines = queryset.all()
    all_amounts = amounts_calculation(all_orderlines)
    total_amount = sum(all_amounts)
    # Post the invoiced order line(s).
    # if request.method == "POST":
    if 0 == 0:  # request.method == "POST"
        # if request.POST.get('post'):  TODO
        # Create the bill instance with the total amount to pay and the user_id
        new_bill = Bill(user_id=request.user, amount=total_amount)
        new_bill.save()
        # Send the bill to the guest's email address.
        emailto = queryset.first().guest_id.email
        guest_name = f"{queryset.first().guest_id.first_name} {queryset.first().guest_id.last_name}"
        formatted_total_amount = f"{total_amount:.2f}"
        send_email(emailto, guest_name, formatted_total_amount)
        # send_email(["lea@vaiatea-liveaboard.com", "william@dragondivekomodo.com"])
        # Collecting all the guest's order line(s) selected.
        orderline_list = request.POST.getlist('_selected_action')
        # Put the new bill id created in the invoiced order line(s) instance(s).
        for orderline in orderline_list:
            orderline_selected = OrderLine.objects.filter(
                id=orderline).last()
            bill_id = Bill.objects.filter(id=new_bill.id).last()
            orderline_selected.bill_id = bill_id
            orderline_selected.save()
        return HttpResponseRedirect('/admin')

    # What to render to the intermediate django admin/bill action template.
    zipped_data = zip(all_orderlines, all_amounts)
    email_selected = all_orderlines[0].guest_id.email
    context = {"orderlines": all_orderlines,
               "zipped_data": zipped_data,
               "total_amount": total_amount,
               "email": email_selected}

    return render(request, 'admin/bill.html', context)


# Payment action to make the payment of a selected bill.
# TODO check qu'il y en a qu'une
@ admin.action(description="Faire le paiement de la facture sélectionnée")
def make_payment(modeladmin, request, queryset):
    """ Admin Action to make the payment of the selected bill ; \
        sending to an intermediate page to display the data ; saving the data \
        into the Payment table."""
    # Send the bill data to display in the payment template that ask for the payment mode.
    bill_info = queryset.all()
    print("POST : ", request.POST.getlist('payment_mode'))
    if "apply" in request.POST:  # TODO Je n'arrive pas à entrer là-dedans
        # Saving the data from the payment form to create an instance in the Payment model.
        # TODO manque info sur mode de payment
        payment_mode = request.POST.cleaned_data['payment_mode']
        new_payment = Payment(user_id=request.user,
                              bill_id=bill_info[0], payment_mode=payment_mode)
        new_payment.save()
        # Mark as a payment done in the Bill model.
        bill_paid = Bill.objects.filter(id=bill_info[0].id).last()
        bill_paid.payment_done = True
        bill_paid.save()

    # What to render to the template.
    payment_form = PaymentForm()
    return render(request, 'admin/payment.html',
                  context={"bill": bill_info, "payment_form": payment_form})


#################################################################################


# ORDERLINE CRUD
@ admin.register(OrderLine)
class OrderLineAdmin(admin.ModelAdmin):
    form = OrderLineForm
    fields = ("guest_id",  "trip_id", ("bar_id", "goodies_id",
              "miscellaneous_id"), "quantity")
    list_display = ("guest_id",  "quantity", "bar_id", "goodies_id",
                    "miscellaneous_id")
    list_filter = ("guest_id",)
    ordering = ("guest_id",)
    search_fields = ("guest_id", "bar_id", "goodies_id", "miscellaneous_id")
    actions = [make_bill]

    def get_queryset(self, request):
        orderline_queryset = super().get_queryset(request)
        return orderline_queryset.filter(bill_id__isnull=True)

    def save_model(self, request, obj, form, change):
        obj.user_id = request.user
        super().save_model(request, obj, form, change)


@ admin.register(InvoicedOrder)
class InvoicedOrderLineAdmin(admin.ModelAdmin):
    exclude = ("user_id", "date", "bill_id")
    list_display = ("guest_id",  "bill_id", "quantity", "bar_id", "goodies_id",
                    "miscellaneous_id")
    list_filter = ("guest_id",)
    ordering = ("guest_id",)
    search_fields = ("guest_id", "bar_id", "goodies_id", "miscellaneous_id")

    def get_queryset(self, request):
        orderline_queryset = super().get_queryset(request)
        return orderline_queryset.filter(bill_id__isnull=False)

    # To disable the add functionality.
    def has_add_permission(self, request):
        return False

    # To disable the change functionality.
    def has_change_permission(self, request, obj=None):
        return False


# BILL CRUD
@ admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ("id", "show_guest", "amount",  "bill_date")
    list_filter = ("bill_date",)
    actions = [make_payment]

    def get_queryset(self, request):
        bill_queryset = super().get_queryset(request)
        return bill_queryset.filter(payment_done="f")

    def show_guest(self, obj):
        invoiced_orderline = OrderLine.objects.filter(bill_id=obj).first()
        guest_billed_ln = invoiced_orderline.guest_id.last_name
        guest_billed_fn = invoiced_orderline.guest_id.first_name
        guest_billed = f"{guest_billed_fn} {guest_billed_ln}"
        return guest_billed

    show_guest.short_description = "Passager.ère"

    def save_model(self, request, obj, form, change):
        obj.user_id = request.user
        super().save_model(request, obj, form, change)

    # To disable the add functionality.
    def has_add_permission(self, request):
        return False

    # To disable the change functionality.
    def has_change_permission(self, request, obj=None):
        return False


@ admin.register(BillPaid)
class BillPaidAdmin(admin.ModelAdmin):
    list_display = ("id", "amount",  "bill_date")
    list_filter = ("bill_date",)

    def get_queryset(self, request):
        bill_queryset = super().get_queryset(request)
        return bill_queryset.filter(payment_done="t")

    # To disable the add functionality.
    def has_add_permission(self, request):
        return False

    # To disable the change functionality.
    def has_change_permission(self, request, obj=None):
        return False


# PAYMENT CRUD
@ admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    exclude = ("user_id", "payment_date")
    list_filter = ("payment_mode", "payment_date")
    ordering = ("payment_date",)

    def save_model(self, request, obj, form, change):
        obj.user_id = request.user
        super().save_model(request, obj, form, change)
