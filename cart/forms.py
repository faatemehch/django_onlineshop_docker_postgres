from django import forms


class AddToCart(forms.Form):
    """A form for adding an item to the shopping cart."""

    QUANTIYY_CHOISES = [(i, str(i)) for i in range(1, 20)]
    quantity = forms.TypedChoiceField(choices=QUANTIYY_CHOISES, coerce=int) # coerce:  str -> int
