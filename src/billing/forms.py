# -*- coding: utf-8 -*-
# pylint: disable=too-few-public-methods
"""Creation of the order form."""

from django.db.models.fields import PositiveSmallIntegerField
from django.forms import (
    BooleanField,
    ModelForm,
    Select,
    TextInput,
)
from django.forms.widgets import NumberInput
from .models import Order


# The order form.
class OrderCreationForm(ModelForm):
    """Form to create the order data form."""

    class Meta:
        """Details of the OrderCreationForm form."""

        model = Order
        exclude = ["user_id", "date"]
        widgets = {
            "guest_id": Select(
                attrs={"class": "form-control form-control-lg",
                       "id": "guest"}
            ),
            "quantity": NumberInput(
                attrs={"class": "form-control form-control-lg",
                       "id": "quantity"}
            ),
        }

        # "payment_mode": Select(
        #     attrs={"class": "form-control form-control-lg",
        #            "id": "paymentMode"}
        # ),
