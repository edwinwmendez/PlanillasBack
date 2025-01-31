# Generated by Django 5.0.6 on 2024-07-15 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auditoria', '0002_initial'),
        ('usuarios', '0002_alter_persona_options_and_more'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='auditoria',
            index=models.Index(fields=['fecha', 'accion'], name='idx_auditoria_fecha_accion'),
        ),
        migrations.AddIndex(
            model_name='auditoria',
            index=models.Index(fields=['persona'], name='idx_auditoria_persona'),
        ),
    ]
