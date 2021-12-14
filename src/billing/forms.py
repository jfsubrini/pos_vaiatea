# -*- coding: utf-8 -*-
# pylint: disable=too-few-public-methods
"""Creation of the order form."""

from django.forms import (
    ModelForm,
    Select,
)
from django import forms
from django.forms.widgets import NumberInput
from .models import OrderLine, Payment


# The orderline form.
class OrderLineCreationForm(ModelForm):
    """Form to create the line of order data form."""

    class Meta:
        """Details of the OrderLineCreationForm form."""

        model = OrderLine
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


# The payment form.
class PaymentForm(ModelForm):
    """Form to create the payment data form."""

    class Meta:
        """Details of the PaymentForm form."""

        model = Payment
        exclude = ["user_id", "amount", "date"]


class EmailForm(forms.Form):
    CHOICES = [('Y', 'Oui'), ('N', 'Non')]
    send_email = forms.CharField(
        widget=forms.RadioSelect(choices=CHOICES))
