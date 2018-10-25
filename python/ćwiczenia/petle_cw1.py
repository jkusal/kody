#!/usr/bin/env python
# -*- coding: utf-8 -*-

def suma(a, b):
    return a + b


def main(args):
    suma = 0
    while suma <= 75:
        liczba = int(input("Podaj liczbę: "))
        suma = liczba + suma
        
    print("Suma: ", suma)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
