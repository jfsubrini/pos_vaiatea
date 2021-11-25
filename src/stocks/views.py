# -*- coding: utf-8 -*-
# pylint: disable=
"""All the views for the stocks app of the pos_vaiatea project.

    """
from django.shortcuts import render


# Stock views
def stock_initial(request):
    """View to the initial stock form page."""
    # To display the empty initial stock form.
    return render(request, "stock_initial.html")


def stock_final(request):
    """View to the final stock form page."""
    # To display the empty final stock form.
    return render(request, "stock_final.html")


def stock_update(request):
    """View to the stock update form page."""
    # To display the empty stock update form.
    return render(request, "stock_update.html")


def stock_list(request):
    """View to the stock list page."""
    # To display the empty stock list.
    return render(request, "stock_list.html")


# Item views
def item_creation(request):
    """View to the item creation form page."""
    # To display the empty item creation form.
    return render(request, "item_creation.html")


def item_update(request):
    """View to the item update form page."""
    # To display the empty item update form.
    return render(request, "item_update.html")


def item_list(request):
    """View to the item list page."""
    # To display the empty item list.
    return render(request, "item_list.html")
