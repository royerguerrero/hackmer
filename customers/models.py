"""Customer model"""

# Django
from django.db import models

# Utils
from hackmer.constants import STATE_CHOICES


class Customer(models.Model):
    name = models.CharField(max_length=100)
    document_id = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    number_phone = models.CharField(max_length=10)
    alternative_number_phone = models.CharField(max_length=10)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str(self):
        return self.name


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)

    state = models.CharField(max_length=100, choices=STATE_CHOICES)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=5)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)