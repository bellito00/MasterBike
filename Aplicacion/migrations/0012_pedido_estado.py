# Generated by Django 5.0.6 on 2024-07-04 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion', '0011_remove_pedido_carrito_pedido_usuario_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='estado',
            field=models.CharField(choices=[('Cancelado', 'Cancelado'), ('En circulacion', 'En circulacion'), ('Entregado', 'Entregado'), ('Pagado', 'Pagado')], default='Sin asignar', max_length=50),
        ),
    ]
