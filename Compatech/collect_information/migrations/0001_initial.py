# Generated by Django 3.0.3 on 2020-05-08 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('categoria_nome', models.CharField(max_length=45, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_pagine', models.IntegerField(default=1)),
                ('link_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collect_information.Categorie')),
            ],
        ),
        migrations.CreateModel(
            name='Siti',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sito_link_base', models.CharField(max_length=200)),
                ('sito_nome', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Prodotti',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pnome', models.CharField(max_length=150)),
                ('brand', models.CharField(max_length=45)),
                ('prezzo', models.CharField(max_length=20)),
                ('link_immagine', models.CharField(max_length=200)),
                ('link_dettaglio', models.CharField(max_length=200)),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collect_information.Links')),
            ],
        ),
        migrations.AddField(
            model_name='links',
            name='link_sito',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collect_information.Siti'),
        ),
    ]