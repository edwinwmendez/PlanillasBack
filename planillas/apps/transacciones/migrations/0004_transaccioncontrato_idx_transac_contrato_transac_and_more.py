# Generated by Django 5.0.6 on 2024-07-15 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0009_configuracionglobal_valorconfiguracionglobal_and_more'),
        ('planillas', '0011_boleta_idx_boleta_contrato_planilla_and_more'),
        ('transacciones', '0003_alter_transaccioncontrato_options_and_more'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='transaccioncontrato',
            index=models.Index(fields=['contrato', 'transaccion'], name='idx_transac_contrato_transac'),
        ),
        migrations.AddIndex(
            model_name='transaccioncontrato',
            index=models.Index(fields=['periodo_inicial', 'periodo_final'], name='idx_transac_contrato_periodo'),
        ),
    ]
