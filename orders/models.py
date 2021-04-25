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

    products = models.ManyToManyField(Product, through='ProductOrder')

    CHOICES_TYPE = [
        ('awaiting_payment', 'Esperando al pago'),
        ('preparing_shipment', 'Preparando para enviar'),
        ('on_the_way', 'En camino'),
        ('no_delivery_confirmation', 'Sin confirmacion de llegada'),
        ('delivery_refused', 'Devuelto'),
        ('delivered', 'Entregado'),
    ]

    status = models.CharField(max_length=50, choices=CHOICES_TYPE)
    observations = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class ProductOrder(models.Model):
    """ProductOrder model"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField()
    price = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
