# Generated by Django 5.0.6 on 2024-07-01 16:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trabajadores', '0003_remove_trabajador_fecha_devengue_and_more'),
        ('usuarios', '0002_alter_persona_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajador',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empleados', to='usuarios.persona', unique=True, verbose_name='Persona'),
        ),
    ]
