# Generated by Django 4.1.7 on 2023-04-24 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_banda_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='banda',
            name='imagen',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='banda',
            name='origen',
            field=models.CharField(max_length=100),
        ),
    ]