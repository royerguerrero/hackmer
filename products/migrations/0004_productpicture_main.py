# Generated by Django 3.1.7 on 2021-03-25 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='productpicture',
            name='main',
            field=models.BooleanField(default=False),
        ),
    ]
