"""Order models"""

# Django
from django.db import models

# Models
from customers.models import Customer, ShippingAddress
from products.models import Product

# Utils
import uuid


class Order(models.Model):
    """Order Model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    shipping_address = models.ForeignKey(ShippingAddress, on_delete=models.SET_NULL, null=True)

    payment_reference = models.CharField(max_length=100, null=True, default=None)

    products = models.ManyToManyField(Product, through='ProductOrder')

    CHOICES_TYPE = [
        ('awaiting_payment', 'Esperando al pago'),
        ('payment_rejected', 'Pago rechazado'),
        ('failed_payment', 'Pago fallido'),
        ('preparing_shipment', 'Preparando para enviar'),
        ('on_the_way', 'En camino'),
        ('no_delivery_confirmation', 'Sin confirmación de llegada'),
        ('delivery_refused', 'Devuelto'),
        ('delivered', 'Entregado'),
    ]

    status = models.CharField(max_length=50, choices=CHOICES_TYPE)
    observations = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def get_order_price(self):
        total = 0
        products_through = self.products.through.objects.filter(order=self.id)

        for product_order in products_through:
            total += product_order.price * product_order.quantity

        return total

    def __str__(self):
        return f'{self.id}[{self.customer.name}]'


class ProductOrder(models.Model):
    """ProductOrder model"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField()
    price = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.quantity} {self.product} for {self.price}'