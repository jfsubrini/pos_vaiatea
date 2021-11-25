# -*- coding: utf-8 -*-
# pylint: disable=
"""All the views for the schedule app of the pos_vaiatea project.

    """
from django.shortcuts import render

from .forms import GuestCreationForm, TripCreationForm
# from .models import Guest, Trip


def guest_creation(request):
    """View to the guest form page."""
    # To display the empty interview forms.
    submitted = False
    guest_form = GuestCreationForm()
    trip_form = TripCreationForm()
    if "submitted" in request.GET:
        submitted = True

    # What to render to the template.
    context = {
        "guest_form": guest_form,
        "trip_form": trip_form,
        "submitted": submitted,
    }

    return render(request, "guest.html", context)
