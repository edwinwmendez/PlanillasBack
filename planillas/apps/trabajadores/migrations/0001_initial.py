# Generated by Django 5.0.6 on 2024-06-30 17:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('configuracion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiempo_servicios', models.CharField(blank=True, max_length=6, verbose_name='Tiempo de Servicios')),
                ('cuspp', models.CharField(blank=True, max_length=12, verbose_name='CUSPP')),
                ('fecha_afiliacion', models.DateField(blank=True, null=True, verbose_name='Fecha de Afiliación')),
                ('fecha_devengue', models.DateField(blank=True, null=True, verbose_name='Fecha de Devengue')),
                ('numero_cuenta', models.CharField(blank=True, max_length=45, verbose_name='Número de Cuenta')),
                ('ruc', models.CharField(blank=True, max_length=11, verbose_name='RUC')),
                ('estado', models.BooleanField(blank=True, default=True, null=True, verbose_name='Estado')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('afp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.afp', verbose_name='AFP')),
                ('banco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.banco', verbose_name='Banco')),
            ],
            options={
                'verbose_name': 'Trabajador',
                'verbose_name_plural': 'Trabajadores',
                'db_table': 'trabajador',
                'ordering': ['id'],
            },
        ),
    ]
