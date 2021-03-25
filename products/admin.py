"""Products admin"""

# Django
from django.contrib import admin

# Models
from products.models import Category, Product, ProductVariation, ProductPicture


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


class ProductVariationInline(admin.StackedInline):
    model = ProductVariation
    min_num = 1
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductVariationInline]


class ProductPictureInline(admin.StackedInline):
    model = ProductPicture
    min_num = 1
    extra = 0


@admin.register(ProductVariation)
class ProductVariationAdmin(admin.ModelAdmin):
    inlines = [ProductPictureInline,]
