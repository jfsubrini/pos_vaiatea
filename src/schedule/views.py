# -*- coding: utf-8 -*-
# pylint: disable=
"""All the views for the schedule app of the pos_vaiatea project.

    """
from django.shortcuts import render

from .forms import GuestCreationForm, TripCreationForm
# from .models import Guest, Trip


# Guest views
def guest_creation(request):
    """View to the guest creation form page."""
    # To display the empty guest creation form.
    submitted = False
    guest_form = GuestCreationForm()
    trip_form = TripCreationForm()
    if "submitted" in request.GET:
        submitted = True

    # What to render to the template.
    context = {
        "guest_form": guest_form,
        "submitted": submitted,
    }

    return render(request, "guest_creation.html", context)


def guest_update(request):
    """View to the guest update form page."""
    # To display the empty guest update form.
    return render(request, "guest_update.html")


def guest_list(request):
    """View to the guest list page."""
    # To display the empty guest list.
    return render(request, "guest_list.html")


# Trip views
def trip_creation(request):
    """View to the trip creation form page."""
    # To display the empty trip creation form.
    submitted = False
    guest_form = GuestCreationForm()
    trip_form = TripCreationForm()
    if "submitted" in request.GET:
        submitted = True

    # What to render to the template.
    context = {
        "trip_form": trip_form,
        "submitted": submitted,
    }

    return render(request, "trip_creation.html", context)


def trip_update(request):
    """View to the trip update form page."""
    # To display the empty trip update form.
    return render(request, "trip_update.html")


def trip_list(request):
    """View to the trip list page."""
    # To display the empty trip list.
    return render(request, "trip_list.html")
