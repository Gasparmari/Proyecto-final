# Generated by Django 4.2 on 2023-04-12 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='banda',
            name='integrantes',
            field=models.TextField(default='some string', max_length=50),
        ),
    ]