#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main(args):
    a = int(input("Podaj liczbę: "))
    while a < 0:
        a = int(input("Podaj liczbę większą od 0: "))
        
    for liczba in range(0, a):
            if not liczba % 2 == 0:
                print(liczba ^ 2)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
