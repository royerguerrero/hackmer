"""Order forms"""

# Django
from django import forms
from django.core.validators import RegexValidator

# Models
from customers.models import Customer, ShippingAddress
from orders.models import Order, Product

# Utils
from hackmer.constants import STATE_CHOICES


class PurchaseForm(forms.Form):
    name = forms.CharField(max_length=100, label='Ingresa tu nombre')
    document_id = forms.CharField(max_length=20, label='Número de documento')
    age = forms.IntegerField(label='Edad')
    email = forms.EmailField(label='Correo electronico')

    regex_phone_number = RegexValidator(r'^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$',
                                        'Ingresa un numero de telefono valido')

    phone_number = forms.CharField(max_length=10, label='Numero de telefono', validators=[regex_phone_number])
    alternative_phone_number = forms.CharField(max_length=10, label='Numero de telefono alternativo', required=False,
                                               validators=[regex_phone_number])

    state = forms.ChoiceField(choices=STATE_CHOICES, label='Departamento')
    city = forms.CharField(max_length=100, label='Ciudad')

    address = forms.CharField(max_length=255, label='Direccion')
    zip_code = forms.CharField(max_length=5, label='Codigo Zip', required=False)

    annotations = forms.CharField(widget=forms.Textarea, label='Observaciones adicionles', required=False)

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18:
            raise forms.ValidationError('Debes ser mayor de edad para poder comprar.')

        return age

    def clean_alternative_phone_number(self):
        alternative_number = self.cleaned_data['alternative_phone_number']
        number = self.cleaned_data['phone_number']

        if alternative_number == number:
            raise forms.ValidationError('El numero alternativo no puede ser el mismo que el numero pincipal')

        return alternative_number

    def save(self):
        data = self.data
        customer = Customer.objects.create(name=data['name'], document_id=data['document_id'],
                                           age=data['age'], email=data['email'])
        shipping_address = ShippingAddress.objects.create(customer=customer, state=data['state'], city=data['city'],
                                                          zip_code=data['zip_code'], address=data['address'])

        order = Order.objects.create(customer=customer, shipping_address=shipping_address,
                                     status='awaiting_payment', observations=data['annotations'])

        # With this i can get a array with the products
        data_dict = dict(data.lists())

        for product in data_dict['products']:
            product = product.split(':')
            queryset_product = Product.objects.get(id=product[0])
            order.products.add(queryset_product,
                               through_defaults={'quantity': int(product[1]), 'price': queryset_product.price - (
                                           queryset_product.price * queryset_product.discount / 100)})

        return order
