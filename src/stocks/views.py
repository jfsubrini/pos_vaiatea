# -*- coding: utf-8 -*-
# pylint: disable=
"""All the views for the stocks app of the pos_vaiatea project.

    """
from django.shortcuts import render

from .forms import (
    BarCreationForm,
    GoodiesCreationForm,
    KitchenCreationForm,
    MiscCreationForm,
)


# Bar views
def bar_creation(request):
    """View to the bar creation form page."""
    # To display the empty bar creation form.
    submitted = False
    bar_create = BarCreationForm()
    if "submitted" in request.GET:
        submitted = True

    # What to render to the template.
    context = {
        "bar_creation": bar_create,
        "submitted": submitted,
    }

    return render(request, "bar_creation.html", context)


def bar_update(request):
    """View to the bar update form page."""
    # To display the empty bar update form.
    return render(request, "bar_update.html")


def bar_list(request):
    """View to the bar list page."""
    # To display the empty bar list.
    return render(request, "bar_list.html")


# Goodies views
def goodies_creation(request):
    """View to the goodies creation form page."""
    # To display the empty goodies creation form.
    submitted = False
    goodies_create = GoodiesCreationForm()
    if "submitted" in request.GET:
        submitted = True

    # What to render to the template.
    context = {
        "goodies_creation": goodies_create,
        "submitted": submitted,
    }

    return render(request, "goodies_creation.html", context)


def goodies_update(request):
    """View to the goodies update form page."""
    # To display the empty goodies update form.
    return render(request, "goodies_update.html")


def goodies_list(request):
    """View to the goodies list page."""
    # To display the empty goodies list.
    return render(request, "goodies_list.html")


# Kitchen views
def kitchen_creation(request):
    """View to the kitchen creation form page."""
    # To display the empty kitchen creation form.
    submitted = False
    kitchen_create = KitchenCreationForm()
    if "submitted" in request.GET:
        submitted = True

    # What to render to the template.
    context = {
        "kitchen_creation": kitchen_create,
        "submitted": submitted,
    }

    return render(request, "kitchen_creation.html", context)


def kitchen_update(request):
    """View to the kitchen update form page."""
    # To display the empty kitchen update form.
    return render(request, "kitchen_update.html")


def kitchen_list(request):
    """View to the kitchen list page."""
    # To display the empty kitchen list.
    return render(request, "kitchen_list.html")


# Miscellaneous views
def misc_creation(request):
    """View to the miscellaneous creation form page."""
    # To display the empty miscellaneous creation form.
    submitted = False
    misc_create = MiscCreationForm()
    if "submitted" in request.GET:
        submitted = True

    # What to render to the template.
    context = {
        "misc_creation": misc_create,
        "submitted": submitted,
    }

    return render(request, "misc_creation.html", context)


def misc_update(request):
    """View to the miscellaneous update form page."""
    # To display the empty miscellaneous update form.
    return render(request, "misc_update.html")


def misc_list(request):
    """View to the miscellaneous list page."""
    # To display the empty miscellaneous list.
    return render(request, "misc_list.html")


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
