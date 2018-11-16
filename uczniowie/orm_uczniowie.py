#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os  
from peewee import * # importuje wszystko 

baza_plik = 'test.db'
baza = SqliteDatabase(baza_plik) # instalacja bazy

### MODELE DANYCH

class BazaModel(Model):
    class Meta:
        database = baza

class Uczen(BazaModel):
    imie = CharField()
    nazwisko = CharField()
    plec = BooleanField()
    id_klasa = IntegerField()
    egzhum = FloatField(default=0)
    egzmat = FloatField(default=0)
    egzjez = FloatField(default=0)
    
        
class Klasa(BazaModel):
    klasa = CharField()
    rok_naboru = DateField()
    rok_matury = DateField()
    
class Przedmiot(BazaModel):
    przedmiot = CharField()
    imie_naucz = CharField()
    nazwisko_naucz = CharField()
    plec_naucz = BooleanField()


class Ocena(BazaModel):
    datad = DateField()
    uczen = ForeignKeyField(Uczen, related_name='wyniki')
    przedmiot = ForeignKeyField(Przedmiot, related_name='coś')
    ocena = IntegerField()

def main(args):
    if os.path.exists(baza_plik):
        os.remove(baza_plik)
    baza.connect() # połączeie z bazą
    baza.create_tables([Uczen, Klasa, Przedmiot, Ocena])
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
