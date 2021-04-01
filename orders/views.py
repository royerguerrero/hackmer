"""Orders views"""

# Django
from django.views.generic import FormView

# Forms
from orders.forms import PurchaseForm


class PurchaseView(FormView):
    template_name = 'orders/purchase.html'
    form_class = PurchaseForm
