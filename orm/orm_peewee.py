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

class Klasa(BazaModel):
    nazwa = CharField(null=False)
    roknaboru = IntegerField(default=0)
    rokmatury = IntegerField(default=0)
    
        
class Uczen(BazaModel):
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    plec = BooleanField()
    klasa = ForeignKeyField(Klasa, related_name='uczniowie')
    
class Wynik(BazaModel):
    egzhum = FloatField(default=0)
    egzmat = FloatField(default=0)
    egzjez = FloatField(default=0)
    uczen = ForeignKeyField(Uczen, related_name='wyniki')
    

def main(args):
    if os.path_exists(baza_plik):
        os.remove(baza_plik)
    baza.connect() # połączeie z bazą
    baza.create_tables([Klasa, Uczen, Wynik])
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
