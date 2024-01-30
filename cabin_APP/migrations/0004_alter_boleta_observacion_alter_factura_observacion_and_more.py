# Generated by Django 4.1.1 on 2023-08-12 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabin_APP', '0003_remove_materiales_proyectos_asociados'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boleta',
            name='observacion',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='factura',
            name='observacion',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='maestro',
            name='observacion',
            field=models.CharField(blank=True, max_length=600),
        ),
        migrations.AlterField(
            model_name='materiales',
            name='observacion',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='observacion',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
    ]