# Generated by Django 5.1.1 on 2024-10-18 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0003_alter_perfil_rol'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dueño',
            name='email',
        ),
    ]
