# Generated by Django 5.2 on 2025-07-07 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmes', '0001_initial'),
        ('genero', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filme',
            name='generos',
            field=models.ManyToManyField(related_name='filmes', to='genero.genero'),
        ),
    ]
