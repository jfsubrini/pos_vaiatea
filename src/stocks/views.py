# -*- coding: utf-8 -*-
# pylint: disable=
"""All the views for the stocks app of the pos_vaiatea project.

    """
from django.shortcuts import render

from .forms import (
    ItemCreationForm,
    DrinkCreationForm,
    GoodiesCreationForm,
    FoodCreationForm
)


# Drink views
def drink_creation(request):
    """View to the drink creation form page."""
    # To display the empty drink creation form.
    submitted = False
    item_create = ItemCreationForm()
    drink_create = DrinkCreationForm()
    if "submitted" in request.GET:
        submitted = True

    # What to render to the template.
    context = {
        "item_creation": item_create,
        "drink_creation": drink_create,
        "submitted": submitted,
    }

    return render(request, "drink_creation.html", context)


def drink_update(request):
    """View to the drink update form page."""
    # To display the empty drink update form.
    return render(request, "drink_update.html")


def drink_list(request):
    """View to the drink list page."""
    # To display the empty drink list.
    return render(request, "drink_list.html")


# Goodies views
def goodies_creation(request):
    """View to the goodies creation form page."""
    # To display the empty goodies creation form.
    submitted = False
    item_create = ItemCreationForm()
    goodies_create = GoodiesCreationForm()
    if "submitted" in request.GET:
        submitted = True

    # What to render to the template.
    context = {
        "item_creation": item_create,
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


# Food views
def food_creation(request):
    """View to the food creation form page."""
    # To display the empty food creation form.
    submitted = False
    item_create = ItemCreationForm()
    food_create = FoodCreationForm()
    if "submitted" in request.GET:
        submitted = True

    # What to render to the template.
    context = {
        "item_creation": item_create,
        "food_creation": food_create,
        "submitted": submitted,
    }

    return render(request, "food_creation.html", context)


def food_update(request):
    """View to the food update form page."""
    # To display the empty food update form.
    return render(request, "food_update.html")


def food_list(request):
    """View to the food list page."""
    # To display the empty food list.
    return render(request, "food_list.html")


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
