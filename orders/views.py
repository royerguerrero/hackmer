"""Orders views"""

# Django
from django.views.generic import FormView
from django.shortcuts import render


class PurchaseView(FormView):
    template_name = 'orders/purchase.html'
