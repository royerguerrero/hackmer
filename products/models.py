"""Products Models"""

# Django
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to='categories/')

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    discount = models.FloatField(default=0)
    video = models.URLField(null=True, blank=True)


class ProductVariation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.CharField(max_length=7, blank=True, null=True, help_text='Hexadecimal colors only')
    height = models.FloatField(blank=True, null=True, help_text='Please add measurement in centimeters.')
    width = models.FloatField(blank=True, null=True, help_text='Please add measurement in centimeters.')
    length = models.FloatField(blank=True, null=True, help_text='Please add measurement in centimeters.')
    weight = models.FloatField(blank=True, null=True, help_text='Please add measurement in centimeters.')
    material = models.CharField(max_length=30, blank=True, null=True)

    SIZE_CHOICES = [
        ('XS', 'XS: Extra Small'),
        ('S', 'S: Small'),
        ('M', 'M: Medium'),
        ('L', 'L: Large'),
        ('XL', 'XL: Extra Large'),
        ('XXL', 'XXL: Extra Extra Large'),
    ]

    size = models.FloatField(blank=True, null=True, choices=SIZE_CHOICES)


class ProductPicture(models.Model):
    product_variation = models.ForeignKey(ProductVariation, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='products/')
