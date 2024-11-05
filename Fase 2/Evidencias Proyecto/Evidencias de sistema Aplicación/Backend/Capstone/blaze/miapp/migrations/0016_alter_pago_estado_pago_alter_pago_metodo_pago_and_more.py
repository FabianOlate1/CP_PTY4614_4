# Generated by Django 4.2 on 2024-11-03 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0015_alter_administrador_asignacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pago',
            name='estado_pago',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('completado', 'Completado'), ('cancelado', 'Cancelado')], max_length=100),
        ),
        migrations.AlterField(
            model_name='pago',
            name='metodo_pago',
            field=models.CharField(choices=[('efectivo', 'Efectivo'), ('tarjeta', 'Tarjeta de Crédito'), ('transferencia', 'Transferencia Bancaria')], max_length=50),
        ),
        migrations.AlterField(
            model_name='pago',
            name='monto',
            field=models.IntegerField(),
        ),
    ]
