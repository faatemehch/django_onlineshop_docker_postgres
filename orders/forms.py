from django import forms
from .models import Order
from django.utils.translation import gettext_lazy as _

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ("first_name", "last_name", "phone_number", "address", "order_note",)
        widgets = {
            'first_name' : forms.TextInput(attrs={'class':'form__input form__input--2', 'id':'billing_fname'}),
            'last_name' : forms.TextInput(attrs={'class':'form__input form__input--2', 'id':'billing_lname'}),
            'phone_number' : forms.TextInput(attrs={'class':'form__input form__input--2',}),
            'address' : forms.Textarea(attrs={'class':'form__input form__input--2 form__input--textarea',}),
            'order_note' : forms.Textarea(attrs={'class':'form__input form__input--2 form__input--textarea','placeholder': _('If You have any note writ here.')}),
        }

