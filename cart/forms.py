from django import forms


class AddToCartForm(forms.Form):
    """A form for adding an item to the shopping cart."""

    QUANTIYY_CHOISES = [(i, str(i)) for i in range(1, 21)]
    quantity = forms.TypedChoiceField(
        choices=QUANTIYY_CHOISES, coerce=int)  # coerce:  str -> int
    inplace = forms.BooleanField(required=False, widget=forms.HiddenInput()) # False: in product_detail, True: in cart
