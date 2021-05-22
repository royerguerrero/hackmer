"""Orders views"""

# Django
from pdb import set_trace
from django.views.generic import FormView, DetailView
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.urls import reverse

# Forms
from orders.forms import PurchaseForm

# Models
from orders.models import Order, ProductOrder


class Purchase(FormView):
    template_name = 'orders/purchase.html'
    form_class = PurchaseForm

    def form_valid(self, form):
        order = form.save()
        return HttpResponseRedirect(f'/pasarela/{order.id}/')


class Payment(DetailView):
    model = Order
    template_name = 'orders/payment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = ProductOrder.objects.filter(order=context['order'])

        return context

@method_decorator(csrf_exempt, name='dispatch')
class OrderStatus(DetailView):
    model = Order
    template_name = 'orders/order_status.html'

    def post(self, request, pk):
        payment_status = int(request.POST.get('x_cod_response', None))

        if payment_status is not None:
            order = self.get_object()
            if payment_status == 1:
                order.status = 'preparing_shipment'
                order.payment_reference = request.POST.get('ref_payco', None)
            elif payment_status == 2:
                order.status = 'payment_rejected'
            elif payment_status == 3:
                order.status = 'awaiting_payment'
            elif payment_status == 4:
                order.status = 'failed_payment'

            order.save()

        return self.get(request, pk)