"""Orders views"""

# Django
from django.views.generic import FormView, DetailView
from django.http import HttpResponseRedirect

# Forms
from orders.forms import PurchaseForm

# Models
from orders.models import Order, ProductOrder


class PurchaseView(FormView):
    template_name = 'orders/purchase.html'
    form_class = PurchaseForm

    def form_valid(self, form):
        order = form.save()
        return HttpResponseRedirect(f'/pasarela/{order.id}/')


class PaymentView(DetailView):
    model = Order
    template_name = 'orders/payment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = ProductOrder.objects.filter(order=context['order'])

        return context