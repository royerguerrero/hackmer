# Generated by Django 3.1.7 on 2021-05-22 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_reference',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('awaiting_payment', 'Esperando al pago'), ('preparing_shipment', 'Preparando para enviar'), ('on_the_way', 'En camino'), ('no_delivery_confirmation', 'Sin confirmación de llegada'), ('delivery_refused', 'Devuelto'), ('delivered', 'Entregado')], max_length=50),
        ),
    ]
