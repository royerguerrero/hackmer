"""Order forms"""

# Django
from django import forms


class PurchaseForm(forms.Form):
    name = forms.CharField(max_length=100)
