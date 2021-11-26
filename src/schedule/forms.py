# -*- coding: utf-8 -*-
# pylint: disable=too-few-public-methods
"""Creation of the guest and trip forms."""

from django.forms import (
    DateInput,
    EmailInput,
    ModelForm,
    Select,
    TextInput,
)
from .models import Guest, Trip


# Changing some widgets (data input for the form).
class DateInputNicer(DateInput):
    """A widget which displays a better DateInput interface to place a date."""

    input_type = "date"


# The guest form.
class GuestCreationForm(ModelForm):
    """Form to create the guest data form."""

    class Meta:
        """Details of the GuestCreationForm form."""

        model = Guest
        exclude = ["created_at", "updated_at"]
        widgets = {
            "first_name": TextInput(
                attrs={"class": "form-control form-control-lg", "id": "firstName"}
            ),
            "last_name": TextInput(
                attrs={"class": "form-control form-control-lg", "id": "lastName"}
            ),
            "nationality": Select(
                attrs={"class": "form-control form-control-lg",
                       "id": "nationality"}
            ),
            "passport_number": TextInput(
                attrs={"class": "form-control form-control-lg",
                       "id": "passportNumber"}
            ),
            "diving_level": Select(
                attrs={"class": "form-control form-control-lg",
                       "id": "divingLevel", "required": False}
            ),
            "email": EmailInput(
                attrs={
                    "class": "form-control form-control-lg",
                    "id": "email",
                    "required": "required",
                }
            ),
            "trips": Select(
                attrs={"class": "form-control form-control-lg",
                       "id": "trips"}
            ),  # TODO
        }

    def __init__(self, *args, **kwargs):  #  TODO
        # To display all the existing itinerary in the database.
        super().__init__(*args, **kwargs)
        self.fields["trips"].queryset = Trip.objects.all()


# The trip form.
class TripCreationForm(ModelForm):
    """Form to create the trip data."""

    class Meta:
        """Details of the TripCreationForm form."""

        model = Trip
        exclude = ["user", "created_at", "updated_at"]
        widgets = {
            "itinerary": Select(
                attrs={"class": "form-control form-control-lg", "id": "itinerary"}
            ),  # TODO
            "duration_days": Select(
                attrs={"class": "form-control form-control-lg",
                       "id": "durationDays"}
            ),
            "starting_date": DateInputNicer(
                attrs={"class": "form-control form-control-lg",
                       "id": "startingDate"}
            ),
            "ending_date": DateInputNicer(
                attrs={"class": "form-control form-control-lg",
                       "id": "endingDate"}
            ),
        }
