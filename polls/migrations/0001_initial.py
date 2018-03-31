# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-03-24 21:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=1000)),
                ('correo', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='TiposDeServicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=1000)),
                ('imagen', models.ImageField(upload_to='services')),
            ],
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=1000)),
                ('apellidos', models.CharField(max_length=1000)),
                ('aniosExperiencia', models.IntegerField()),
                ('telefono', models.CharField(max_length=1000)),
                ('correo', models.CharField(max_length=1000)),
                ('imagen', models.ImageField(upload_to='photos')),
                ('tiposDeServicio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.TiposDeServicio')),
                ('usuarioId', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comentario',
            name='trabajador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Trabajador'),
        ),
    ]
