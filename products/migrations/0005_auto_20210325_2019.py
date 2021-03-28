# Generated by Django 3.1.7 on 2021-03-25 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_productpicture_main'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='a', unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='a', unique=True),
            preserve_default=False,
        ),
    ]
