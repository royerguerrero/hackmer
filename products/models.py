"""Products Models"""

# Django
from django.db import models
from django.contrib.postgres.fields import ArrayField


class Category(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=70)
    description = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to='categories/')

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    features = ArrayField(models.CharField(max_length=150), null=True, blank=True)
    price = models.FloatField()
    discount = models.IntegerField(default=0)
    video = models.URLField(null=True, blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def get_main_picture(self):
        return ProductPicture.objects.filter(main=True, product=self).first()

    def get_pictures(self):
        pictures = ProductPicture.objects.filter(product=self)
        return pictures

    def __str__(self):
        """Returns name to product"""
        return self.name


class ProductPicture(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    main = models.BooleanField(default=False)
    picture = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.picture.url
