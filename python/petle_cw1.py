#!/usr/bin/env python
# -*- coding: utf-8 -*-

def suma(a, b):
    return a + b


def main(args):
    a = int(input("Podaj liczbę a: "))
    b = int(input("Podaj liczbę b: "))
    while a + b > 75:
        suma(a, b) = int(input("Suma większa niż 75."))
        
    for liczba in range(a, b):
        print("Suma: ", suma(a, b))
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
