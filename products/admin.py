"""Products admin"""

# Django
from django.contrib import admin

# Models
from products.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
