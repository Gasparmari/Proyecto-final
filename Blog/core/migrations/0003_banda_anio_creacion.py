# Generated by Django 4.2 on 2023-04-12 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_banda_integrantes'),
    ]

    operations = [
        migrations.AddField(
            model_name='banda',
            name='anio_creacion',
            field=models.TextField(default='some string', max_length=50),
        ),
    ]
