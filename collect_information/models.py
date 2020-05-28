from django.db import models

class Prodotti(models.Model):
    nome = models.CharField(max_length=150)
    brand = models.CharField(max_length=45)
    prezzo = models.CharField(max_length=20)
    link_immagine = models.CharField(max_length=200)
    link_dettaglio = models.CharField(max_length=200)
    link = models.ForeignKey('Links', on_delete=models.CASCADE)

class Siti(models.Model):
    sito_link_base = models.CharField(max_length=200)
    sito_nome = models.CharField(max_length=45)

class Categorie(models.Model):
    categoria_nome = models.CharField(max_length=45, primary_key=True)

class Links(models.Model):
    link = models.CharField(max_length=150, default='needed')
    sito = models.ForeignKey('Siti', on_delete=models.CASCADE)
    categoria = models.ForeignKey('Categorie', on_delete=models.CASCADE)
    numero_pagine = models.IntegerField(default=1)




