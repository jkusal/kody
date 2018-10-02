#!/usr/bin/env python
# -*- coding: utf-8 -*-
# DANE WEJŚCIOWE: liczba "l2" co najmniej 2-cyfrowa podawana przez użytkownika
#DANE WYJŚCIOWE: suma cyfr liczby "l2" wydrukowana w terminalu


def main(args):
    
    suma = 0
    
    l2 = int(input("Podaj liczbę: "))
    while l2 < 10:
        l2 = int(input("Podaj liczbę co najmniej dwucyfrową: "))
        
   
        
    while l2 > 0:
        suma += l2 % 10
        l2 = int(l2 / 10)
            
    print("Suma cyfr: ", suma)
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
