# Generated by Django 5.0.6 on 2024-07-03 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion', '0007_alter_comuna_region_delete_region'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='comuna',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='comprador',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='productos',
        ),
        migrations.RemoveField(
            model_name='pedidoproducto',
            name='pedido',
        ),
        migrations.RemoveField(
            model_name='pedidoproducto',
            name='producto',
        ),
        migrations.DeleteModel(
            name='Comuna',
        ),
        migrations.DeleteModel(
            name='Persona',
        ),
        migrations.DeleteModel(
            name='Pedido',
        ),
        migrations.DeleteModel(
            name='PedidoProducto',
        ),
    ]
