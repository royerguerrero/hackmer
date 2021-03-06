# Generated by Django 3.1.7 on 2021-03-26 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_features'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productpicture',
            name='product_variation',
        ),
        migrations.AddField(
            model_name='productpicture',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.product'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ProductVariation',
        ),
    ]
