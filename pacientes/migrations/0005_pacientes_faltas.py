# Generated by Django 5.1.6 on 2025-02-18 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0004_visualizacoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='pacientes',
            name='faltas',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
