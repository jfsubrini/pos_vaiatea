# -*- coding: utf-8 -*-
# pylint: disable=too-few-public-methods
"""Creation of the order form."""

from django.forms import (
    ModelForm,
)
from django import forms
from .models import OrderLine, Payment


# The orderline form.
class OrderLineForm(ModelForm):
    """Form to create the line of order data form."""

    class Meta:
        """Details of the OrderLineCreationForm form."""

        model = OrderLine
        fields = '__all__'

    def clean(self):
        cleaned_data = self.cleaned_data
        bar_id = cleaned_data.get('bar_id')
        goodies_id = cleaned_data.get('goodies_id')
        miscellaneous_id = cleaned_data.get('miscellaneous_id')
        quantity = cleaned_data.get('quantity')
        if quantity == 0:
            raise forms.ValidationError(
                "Il faut mettre une quantité supérieure à 0.")
        if bar_id:
            if not goodies_id and not miscellaneous_id:
                pass
            else:
                raise forms.ValidationError(
                    "Ne choisir qu'un seul article : une boisson, un goody \
                        ou un autre article divers.")
        elif goodies_id:
            if miscellaneous_id:
                raise forms.ValidationError(
                    "Ne choisir qu'un seul article : une boisson, un goody \
                        ou un autre article divers.")
        elif miscellaneous_id:
            pass
        else:
            raise forms.ValidationError(
                "Il faut sélectionner au moins un article.")


# The payment form.
class PaymentForm(ModelForm):
    """Form to create the payment data form."""

    class Meta:
        """Details of the PaymentForm form."""

        model = Payment
        exclude = ["user_id", "bill_id", "amount", "date"]
