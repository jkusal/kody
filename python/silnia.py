#!/usr/bin/env python
# -*- coding: utf-8 -*-
  
def silnia_it(a):
    # 0! = 1 
    # n! = 1 * 2 * ... * n
    wynik = 1
    for i in range(a):
        print(wynik)
        wynik = wynik * (i + 1)
    return wynik
    
def main(args):
    a = int(input("Podaj liczbę: "))
    print("{}! = {}".format(a, silnia_it(a)))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
