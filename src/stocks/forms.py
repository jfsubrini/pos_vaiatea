# -*- coding: utf-8 -*-
# pylint: disable=too-few-public-methods
"""Creation of the drink, goodies and food forms."""

from django.forms import (
    ModelForm,
    Select,
    TextInput,
    NumberInput,
)
from .models import Bar, Goodies, Kitchen, Miscellaneous


# The bar form.
class BarCreationForm(ModelForm):
    """Form to create the bar data form."""

    class Meta:
        """Details of the BarCreationForm form."""

        model = Bar
        exclude = ["user_id"]


# The goodies form.
class GoodiesCreationForm(ModelForm):
    """Form to create the goodies data form."""

    class Meta:
        """Details of the GoodiesCreationForm form."""

        model = Goodies
        exclude = ["user_id"]


# The kitchen form.
class KitchenCreationForm(ModelForm):
    """Form to create the kitchen data form."""

    class Meta:
        """Details of the KitchenCreationForm form."""

        model = Kitchen
        exclude = ["user_id"]


# The miscellaneous form.
class MiscCreationForm(ModelForm):
    """Form to create the miscellaneous data form."""

    class Meta:
        """Details of the MiscellaneousCreationForm form."""

        model = Miscellaneous
        exclude = ["user_id"]
