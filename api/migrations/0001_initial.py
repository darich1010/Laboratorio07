# Generated by Django 5.2.3 on 2025-06-25 20:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de la categoría')),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del producto')),
                ('descripcion', models.TextField(blank=True, verbose_name='Descripción')),
                ('precio', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Precio (S/.)')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.categoria', verbose_name='Categoría')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
    ]
