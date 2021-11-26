# -*- coding: utf-8 -*-
# pylint: disable=too-few-public-methods
"""Creation of the order form."""

from django.forms import (
    BooleanField,
    ModelForm,
    Select,
    TextInput,
)
from .models import Order


# The order form.
class OrderCreationForm(ModelForm):
    """Form to create the order data form."""

    class Meta:
        """Details of the OrderCreationForm form."""

        model = Order
        exclude = ["date"]
        widgets = {
            "miscellaneous": TextInput(
                attrs={"class": "form-control form-control-lg",
                       "id": "miscellaneous"}
            ),
            "payment_mode": Select(
                attrs={"class": "form-control form-control-lg",
                       "id": "paymentMode"}
            ),
            # "payment_done": BooleanField(
            #     attrs={"class": "form-control form-control-lg",
            #            "id": "paymentDone"}
            # ),
            # "trips": Select(
            #     attrs={"class": "form-control form-control-lg",
            #            "id": "trips"}
            # ),  # TODO
        }
