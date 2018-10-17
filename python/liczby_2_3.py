#!/usr/bin/env python
# -*- coding: utf-8 -*-


def liczby2(a=10, b=99):
    
    """
    Program drukuje wszystkie liczby dwucyfrowe o niepowtarzających się
    cyfrach oraz zwraca ilość takich liczb
    """
    ile = 0
    
    for i in range(1, 10):
        for j in range(0, 10):
            if i != j:
                print("{}{} ".format(i,j), end='')
                ile += 1
    return ile
			          
        
    
def liczby3(a=100, b=999):
    
    """
    Program drukuje wszystkie liczby trzycyfrowe o niepowtarzających się
    cyfrach oraz zwraca ilość takich liczb
    """
    
    ile = 0
    
    for i in range(1, 10):
        for j in range(0, 10):
            for k in range(0.10):
                if i != j & i != k & j != k:
                    print("{}{} ".format(i,j,k), end='')
                    ile += 1
    return ile

def main(args):
    
    print(liczby3())
    
    return 0

if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
