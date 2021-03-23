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