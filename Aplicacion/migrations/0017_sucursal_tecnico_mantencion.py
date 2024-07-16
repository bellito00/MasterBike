# Generated by Django 5.0.6 on 2024-07-15 22:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion', '0016_pedido_apellido_receptor_pedido_comuna_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tecnico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mantencion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('valor', models.IntegerField()),
                ('imagen', models.ImageField(null=True, upload_to='Aplicacion/media/productos')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('sucursal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Aplicacion.sucursal')),
                ('tecnico', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Aplicacion.tecnico')),
            ],
        ),
    ]