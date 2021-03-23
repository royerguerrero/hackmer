"""Hackmer Views"""

# Django
from django.views.generic import ListView, TemplateView

# Models
from products.models import Category


class IndexView(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'home.html'


class Cookies(TemplateView):
    template_name = 'legality/cookies.html'


class DataHandling(TemplateView):
    template_name = 'legality/data.html'


class ReturnProducts(TemplateView):
    template_name = 'legality/returns.html'