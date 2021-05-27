"""Hackmer sitesmaps"""

# Django
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

# Models
from products.models import Product, Category


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['home', 'data', 'cookies', 'returns']

    def location(self, item):
        return reverse(item)


class ProductSitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return Product.objects.filter(status=True)

    def lastmod(self, obj):
        return obj.modified_at

    def location(self, obj):
        return f'/productos/{obj.slug}/'


class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Category.objects.all()

    def lastmod(self, obj):
        return obj.modified_at

    def location(self, obj):
        return f'/categoria/{obj.slug}/'
