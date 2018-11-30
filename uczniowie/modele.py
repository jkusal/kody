#!/usr/bin/env python
# -*- coding: utf-8 -*-
from peewee import * # importuje wszystko 

baza_plik = 'test.db'
baza = SqliteDatabase(baza_plik) # instalacja bazy

### MODELE DANYCH

class BazaModel(Model):
    class Meta:
        database = baza

class Klasa(BazaModel):
    klasa = CharField()
    rok_naboru = DateField()
    rok_matury = DateField()

class Uczen(BazaModel):
    imie = CharField()
    nazwisko = CharField()
    plec = IntegerField()
    klasa = ForeignKeyField(Klasa, related_name='uczniowie')
    egzhum = FloatField(default=0)
    egzmat = FloatField(default=0)
    egzjez = FloatField(default=0)
    
    
class Przedmiot(BazaModel):
    przedmiot = CharField()
    imie_naucz = CharField()
    nazwisko_naucz = CharField()
    plec_naucz = IntegerField()


class Ocena(BazaModel):
    datad = DateField()
    uczen = ForeignKeyField(Uczen, related_name='oceny')
    przedmiot = ForeignKeyField(Przedmiot, related_name='oceny')
    ocena = FloatField(null=False)
