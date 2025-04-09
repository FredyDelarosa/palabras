# Generated by Django 5.2 on 2025-04-08 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Palabra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=100)),
                ('nivel', models.IntegerField(choices=[(1, 'Letras'), (2, 'Palabras Incompletas'), (3, 'Palabras Completas con Pista')])),
                ('pista', models.CharField(blank=True, max_length=255, null=True)),
                ('imagen_url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
