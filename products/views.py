"""Products Views"""

# Django
from django.views.generic import DetailView

# Models
from products.models import Category, Product


class CategoryDetail(DetailView):
    template_name = 'categories/detail.html'
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        products = Product.objects.filter(category=super().get_object())
        context['products'] = products
        return context


class ProductDetail(DetailView):
    template_name = 'products/detail.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['images'] = context['product'].get_pictures()

        return context
