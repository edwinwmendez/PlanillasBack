# Generated by Django 5.0.6 on 2024-06-27 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planillas', '0003_contrato_delete_planillatrabajador'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fuentefinanciamiento',
            name='tipo_planilla',
        ),
        migrations.AddField(
            model_name='fuentefinanciamiento',
            name='codigo_fuente_financiamiento',
            field=models.CharField(blank=True, max_length=2, verbose_name='Código de Fuente de Financiamiento'),
        ),
    ]
