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
    if os.path.exists(baza_plik):
        os.remove(baza_plik)
    baza.connect() # połączeie z bazą
    baza.create_tables([Klasa, Uczen, Wynik])
        
    kl2A = Klasa(nazwa="2A", roknaboru=2010, rokmatury=2013)
    kl2A.save()
    
    u1 = Uczen(imie="Jarosław", nazwisko="Maly", plec=False, klasa=kl2A)
    u1.save()
    
    kl1A = Klasa(nazwa="1A", roknaboru=2009, rokmatury=2012)
    kl1A.save()
    
    u2 = Uczen(imie="Anna", nazwisko="Gacek", plec=True, klasa=kl1A)
    u2.save()
    
    u3 = Uczen(imie="Roman", nazwisko="Polek", plec=False, klasa=kl1A)
    u3.save()
    
    uczniowie = Uczen.select()
    for uczen in uczniowie:
        print(uczen.id, uczen.nazwisko, uczen.klasa.nazwa)
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
