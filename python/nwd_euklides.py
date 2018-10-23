#!/usr/bin/env python
# -*- coding: utf-8 -*-
  
def NWD_klasyczny(a, b):
    
    licznik = 0
    while a != b:
        if a > b:
            a -= b
            licznik += 1
        else:
            b -= a
            licznik += 1
    print("Powtórzeń:", licznik)
    return a
    
def main(args):
    a = int(input("Podaj liczbę a: "))
    b = int(input("Podaj liczbę b: "))
    
    print(NWD_klasyczny(a, b))
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
