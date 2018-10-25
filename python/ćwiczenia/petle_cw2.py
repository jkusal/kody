#!/usr/bin/env python
# -*- coding: utf-8 -*-
 


def main(args):
    a = int(input("Podaj liczbę: ")) 
    b = int(input("Podaj liczbę: "))
    
    while a >= b:
        b = int(input("Podaj większą liczbę niż pierwsza! Liczba 2: "))
		
    
    if a <= b:
        for liczba in range(a, b + 1):
                print(liczba, end = " ")
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
