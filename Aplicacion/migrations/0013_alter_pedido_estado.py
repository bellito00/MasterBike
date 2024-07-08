# Generated by Django 5.0.6 on 2024-07-06 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion', '0012_pedido_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='estado',
            field=models.CharField(choices=[('Cancelado', 'Cancelado'), ('En circulacion', 'En circulacion'), ('Entregado', 'Entregado'), ('Pagado', 'Pagado')], default='Pagado', max_length=50),
        ),
    ]
