# Generated by Django 5.0.6 on 2024-06-30 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='persona',
            options={'ordering': ['apellido_paterno', 'apellido_materno', 'nombres'], 'verbose_name': 'Persona', 'verbose_name_plural': 'Personas'},
        ),
        migrations.RenameField(
            model_name='persona',
            old_name='materno',
            new_name='apellido_materno',
        ),
        migrations.RenameField(
            model_name='persona',
            old_name='paterno',
            new_name='apellido_paterno',
        ),
    ]
