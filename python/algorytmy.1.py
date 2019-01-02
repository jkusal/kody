#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  algorytmy.1.py
#  
#  Copyright 2019  <>  


def main(args):
    
    n = int(input("Podaj liczbę: "))
    i = 1
    for i in range(i, n, 2):
        print(i)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
#algorytm częściowo poprawny, skończony, o złożoności liniowej O(n)
