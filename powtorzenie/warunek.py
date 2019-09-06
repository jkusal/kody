#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  warunek.py
#  
#  Copyright 2019  <> 
#  


def main(args):
    
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))
    c = int(input("Podaj trzecią liczbę: "))
    
    if a > b and a > c:
        a = max
    if b > a and b > c:
        max = b
    else: 
        max = c
    
    print("Największa wprowadzona liczba: ", max)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
