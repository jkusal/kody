#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os  
from modele import *

def dodaj_dane(dane):
    for model, plik in dane.items():
        print(plik)
        
        model.insert_many()

def main(args):
    if os.path.exists(baza_plik):
        os.remove(baza_plik)
    baza.connect() # połączeie z bazą
    baza.create_tables([Klasa, Uczen, Przedmiot, Ocena])
    
    dane = {
        Klasa: 'klasy',
        Uczen: 'uczniowie',
        Przedmiot: 'przedmioty',
        Ocena: 'oceny',
    }
    dodaj_dane(dane)
    baza.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
