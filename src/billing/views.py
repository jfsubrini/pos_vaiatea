# -*- coding: utf-8 -*-
# pylint: disable=
"""All the views for the billing app of the pos_vaiatea project.

    """
from django.shortcuts import render

from .forms import OrderLineCreationForm, PaymentForm


# OrderLine views
# def orderline_creation(request):
#     """View to the order line creation form page."""
#     # To display the empty order line creation form.
#     submitted = False
#     orderline_create = OrderLineCreationForm()
#     if "submitted" in request.GET:
#         submitted = True

#     # What to render to the template.
#     context = {
#         "orderline_creation": orderline_create,
#         "submitted": submitted,
#     }

#     return render(request, "orderline_creation.html", context)


# def orderline_update(request):
#     """View to the order line update form page."""
#     # To display the empty order line update form.
#     return render(request, "orderline_update.html")


# def bill_editing(request):
#     """View to the bill editing page."""
#     # To display the empty bill editing page.
#     return render(request, "bill_editing.html")


# # User views
# def user_creation(request):
#     """View to the user creation form page."""
#     # To display the empty user creation form.
#     return render(request, "user_creation.html")


# def user_update(request):
#     """View to the user update form page."""
#     # To display the empty user update form.
#     return render(request, "user_update.html")


# def user_list(request):
#     """View to the user list page."""
#     # To display the empty user list.
#     return render(request, "user_list.html")


# # Payment views
# def payment(request):
#     """View to the payment form page."""
#     # To display the empty payment form.
#     submitted = False
#     payment = PaymentForm()
#     if "submitted" in request.GET:
#         submitted = True

#     # What to render to the template.
#     context = {
#         "payment": payment,
#         "submitted": submitted,
#     }

#     return render(request, "payment.html", context)


# def payment_list(request):
#     """View to the payment list page."""
#     # To display the empty payment list page.
#     return render(request, "payment_list.html")
