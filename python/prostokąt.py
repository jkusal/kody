#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Dane wejścia: boki a i b prostokąta
#  Dane wyjściowe: prostokąt utworzony z gwiazdek o rozmiarach podanych przez użytkownika
#  EXTRA: znak, ktorym rysowany jest prostokąt, pobierz od użytkownika


def main(args):
    
    a = int(input("Podaj bok a: ")) 
    b = int(input("Podaj bok b: "))
    
    for i in range(a):
        if i == 0  or i == a - 1:
            print("*"*b)
            continue
        for j in range(b):
            if j > 0  and j < b - 1:
                print(" ", end='')
            else:
                print("*", end='')
            
        print()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
