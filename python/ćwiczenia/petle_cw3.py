#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main(args):
    
    iloczyn = 0
    
    a = int(input("Podaj liczbę końcową zakresu: "))
    
    for liczba in range(0, a + 1):
		iloczyn = liczba * liczba
		print(iloczyn)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
