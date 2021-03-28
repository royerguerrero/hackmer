"""Products admin"""

# Django
from django.contrib import admin

# Models
from products.models import Category, Product, ProductPicture


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


class ProductPictureInline(admin.StackedInline):
    model = ProductPicture
    min_num = 1
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductPictureInline,]