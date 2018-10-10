#!/usr/bin/env python
# -*- coding: utf-8 -*-
  
def NWD_klasyczny(a, b):
    
    while a == b:
        return a
    while a > b:
        a = a - b
        else:
            a = b - a
    
    return nwd
    
def main(args):
    a = int(input("Podaj liczbę a: "))
    b = int(input("Podaj liczbę b: "))
    
    print(NWD_klasyczny(a, b))
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
