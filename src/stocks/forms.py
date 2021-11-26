# -*- coding: utf-8 -*-
# pylint: disable=too-few-public-methods
"""Creation of the drink, goodies and food forms."""

from django.forms import (
    ModelForm,
    Select,
    TextInput,
    NumberInput,
)
from .models import Drink, Goodies, Food


# The drink form.
class DrinkCreationForm(ModelForm):
    """Form to create the drink data form."""

    class Meta:
        """Details of the DrinkCreationForm form."""

        model = Drink
        exclude = ["created_at", "updated_at"]
        widgets = {
            "price_unit_dollar": NumberInput(
                attrs={"class": "form-control form-control-lg", "id": "priceUnitDollar",
                       }
            ),
        }


# The goodies form.
class GoodiesCreationForm(ModelForm):
    """Form to create the goodies data form."""

    class Meta:
        """Details of the GoodiesCreationForm form."""

        model = Goodies
        exclude = ["created_at", "updated_at"]
        widgets = {
            "category": Select(
                attrs={"class": "form-control form-control-lg",
                       "id": "category"}
            ),
            "size": Select(
                attrs={"class": "form-control form-control-lg",
                       "id": "size"}
            ),
            "color": TextInput(
                attrs={"class": "form-control form-control-lg", "id": "color"}
            ),
            "gender": Select(
                attrs={"class": "form-control form-control-lg",
                       "id": "gender"}
            ),
            "price_unit_dollar": NumberInput(
                attrs={"class": "form-control form-control-lg", "id": "priceUnitDollar",
                       }
            ),
        }


# The food form.
class FoodCreationForm(ModelForm):
    """Form to create the food data form."""

    class Meta:
        """Details of the FoodCreationForm form."""

        model = Food
        exclude = ["created_at", "updated_at"]
        widgets = {
            "food_category": Select(
                attrs={"class": "form-control form-control-lg",
                       "id": "foodCategory"}
            ),
        }
