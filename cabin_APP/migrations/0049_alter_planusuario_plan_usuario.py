# Generated by Django 4.1.1 on 2023-11-19 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabin_APP', '0048_remove_planusuario_admin_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planusuario',
            name='plan_usuario',
            field=models.CharField(choices=[('Mensual', 'Mensual'), ('3 Meses', '3 Meses'), ('Anual', 'Anual'), ('5 años', '5 años')], default='Mensual', max_length=10),
        ),
    ]