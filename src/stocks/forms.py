# -*- coding: utf-8 -*-
# pylint: disable=too-few-public-methods
"""Creation of the intial and final stock for bar, kitchen and goodies items."""

from django.forms import ModelForm
from .models import Bar, Goodies, Kitchen


class BarStockForm(ModelForm):
    """Form to create initial bar stock form."""

    class Meta:
        """Details of the BarStockForm form."""

        model = Bar
        exclude = ["user_id", "created_at", "updated_at"]
        # widgets = {
        #     "first_name": TextInput(
        #         attrs={"class": "form-control form-control-lg",
        #                "id": "firstName"}
        #     ),
        # }


class KitchenStockForm(ModelForm):
    """Form to create initial kitchen stock form."""

    class Meta:
        """Details of the KitchenStockForm form."""

        model = Kitchen
        exclude = ["user_id", "created_at", "updated_at"]
        # widgets = {
        #     "first_name": TextInput(
        #         attrs={"class": "form-control form-control-lg",
        #                "id": "firstName"}
        #     ),
        # }


class GoodiesStockForm(ModelForm):
    """Form to create initial goodies stock form."""

    class Meta:
        """Details of the GoodiesStockForm form."""

        model = Goodies
        exclude = ["user_id", "created_at", "updated_at"]
        # widgets = {
        #     "first_name": TextInput(
        #         attrs={"class": "form-control form-control-lg",
        #                "id": "firstName"}
        #     ),
        # }
