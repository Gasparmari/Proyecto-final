# Generated by Django 4.2 on 2023-04-12 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_banda_anio_creacion_alter_banda_integrantes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banda',
            name='integrantes',
            field=models.CharField(default='', max_length=50),
        ),
    ]
