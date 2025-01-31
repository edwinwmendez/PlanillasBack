# Generated by Django 5.0.6 on 2024-07-01 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planillas', '0005_alter_contrato_options_contrato_centro_de_trabajo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boleta',
            name='descargada',
            field=models.BooleanField(default=False, editable=False, verbose_name='Descargada'),
        ),
        migrations.AlterField(
            model_name='boleta',
            name='fecha_descarga',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Fecha de Descarga'),
        ),
        migrations.AlterField(
            model_name='boleta',
            name='fecha_visualizacion',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Fecha de Visualización'),
        ),
        migrations.AlterField(
            model_name='boleta',
            name='neto_a_pagar',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=12, verbose_name='Neto a Pagar'),
        ),
        migrations.AlterField(
            model_name='boleta',
            name='numero_boleta',
            field=models.CharField(editable=False, max_length=3, unique=True, verbose_name='Número de Boleta'),
        ),
        migrations.AlterField(
            model_name='boleta',
            name='total_aportes',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=12, verbose_name='Total Aportes'),
        ),
        migrations.AlterField(
            model_name='boleta',
            name='total_descuentos',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=12, verbose_name='Total Descuentos'),
        ),
        migrations.AlterField(
            model_name='boleta',
            name='total_haberes',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=12, verbose_name='Total Haberes'),
        ),
        migrations.AlterField(
            model_name='boleta',
            name='visualizada',
            field=models.BooleanField(default=False, editable=False, verbose_name='Visualizada'),
        ),
    ]
