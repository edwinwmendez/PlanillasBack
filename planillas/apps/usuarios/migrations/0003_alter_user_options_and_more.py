# Generated by Django 5.0.6 on 2024-07-15 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('configuracion', '0009_configuracionglobal_valorconfiguracionglobal_and_more'),
        ('trabajadores', '0006_rename_persona_idx_idx_trabajador_persona_and_more'),
        ('usuarios', '0002_alter_persona_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.AddIndex(
            model_name='beneficiario',
            index=models.Index(fields=['trabajador'], name='idx_beneficiario_trabajador'),
        ),
        migrations.AddIndex(
            model_name='beneficiario',
            index=models.Index(fields=['estado'], name='idx_beneficiario_estado'),
        ),
        migrations.AddIndex(
            model_name='persona',
            index=models.Index(fields=['numero_documento'], name='idx_persona_documento'),
        ),
        migrations.AddIndex(
            model_name='persona',
            index=models.Index(fields=['apellido_paterno', 'apellido_materno', 'nombres'], name='idx_persona_nombre_completo'),
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['role'], name='idx_user_role'),
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['ugel'], name='idx_user_ugel'),
        ),
    ]
