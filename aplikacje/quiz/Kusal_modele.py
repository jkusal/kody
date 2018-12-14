#!/usr/bin/env python
# -*- coding: utf-8 -*-
from peewee import * # importuje wszystko 
import os  

baza_plik = 'test.db'
baza = SqliteDatabase(baza_plik) # instalacja bazy

### MODELE DANYCH

class BazaModel(Model):
    class Meta:
        database = baza

class Kategoria(BazaModel):
    kategoria = CharField()

class Pytanie(BazaModel):
    pytanie = CharField()
    kat = ForeignKeyField(Kategoria, related_name='kategorie')
    
class Odpowiedz(BazaModel):
    p = ForeignKeyField(Pytanie, related_name='pytania')
    odpowiedz = CharField()
    odpok = FloatField(default=0)


def main(args):
    if os.path.exists(baza_plik):
        os.remove(baza_plik)
    baza.connect() # połączeie z bazą
    baza.create_tables([Kategoria, Pytanie, Odpowiedz])
    
    baza.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
