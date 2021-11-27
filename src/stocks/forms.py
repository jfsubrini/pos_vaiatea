# -*- coding: utf-8 -*-
# pylint: disable=too-few-public-methods
"""Creation of the drink, goodies and food forms."""

from django.forms import (
    ModelForm,
    Select,
    TextInput,
    NumberInput,
)
from .models import Item, Drink, Goodies, Food, Miscellaneous


# Name input for the forms.
class ItemCreationForm(ModelForm):
    """Form to create the name data for the drink, goodies and food forms."""

    class Meta:
        """Details of the ItemCreationForm form."""

        model = Item
        exclude = ["drink_id", "goodies_id", "food_id",
                   "miscellaneous_id", "user_id", "created_at", "updated_at"]
        widgets = {
            "name": TextInput(
                attrs={"class": "form-control form-control-lg", "id": "name",
                       }
            ),
        }


# The drink form.
class DrinkCreationForm(ModelForm):
    """Form to create the drink data form."""

    class Meta:
        """Details of the DrinkCreationForm form."""

        model = Drink
        fields = '__all__'
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
        fields = '__all__'
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
        fields = '__all__'
        widgets = {
            "food_category": Select(
                attrs={"class": "form-control form-control-lg",
                       "id": "foodCategory"}
            ),
        }


# The miscellaneous form.
class MiscCreationForm(ModelForm):
    """Form to create the miscellaneous data form."""

    class Meta:
        """Details of the MiscellaneousCreationForm form."""

        model = Miscellaneous
        fields = '__all__'
        widgets = {
            "price_unit_dollar": NumberInput(
                attrs={"class": "form-control form-control-lg", "id": "priceUnitDollar",
                       }
            ),
        }
