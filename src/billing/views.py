# -*- coding: utf-8 -*-
# pylint: disable=
"""All the views for the billing app of the pos_vaiatea project.

    """
from django.shortcuts import render

from .forms import OrderCreationForm


# Order views
def order_creation(request):
    """View to the order creation form page."""
    # To display the empty order creation form.
    submitted = False
    order_create = OrderCreationForm()
    if "submitted" in request.GET:
        submitted = True

    # What to render to the template.
    context = {
        "order_creation": order_create,
        "submitted": submitted,
    }

    return render(request, "order_creation.html", context)


def order_update(request):
    """View to the order update form page."""
    # To display the empty order update form.
    return render(request, "order_update.html")


def bill_editing(request):
    """View to the bill editing page."""
    # To display the empty bill editing page.
    return render(request, "bill_editing.html")


# User views
def user_creation(request):
    """View to the user creation form page."""
    # To display the empty user creation form.
    return render(request, "user_creation.html")


def user_update(request):
    """View to the user update form page."""
    # To display the empty user update form.
    return render(request, "user_update.html")


def user_list(request):
    """View to the user list page."""
    # To display the empty user list.
    return render(request, "user_list.html")
