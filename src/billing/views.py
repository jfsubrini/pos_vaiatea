# -*- coding: utf-8 -*-
# pylint: disable=
"""All the views for the billing app of the pos_vaiatea project.

    """
from django.shortcuts import render


# Order views
def order_creation(request):
    """View to the order creation form page."""
    # To display the empty order creation form.
    return render(request, "order_creation.html")


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
