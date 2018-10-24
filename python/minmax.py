#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random



def minmax1():
    a = int(input("Podaj liczbę: "))
    min = a
    max = a
    
    while True:
        a = int(input("Podaj liczbę: "))
        if a < 1:
            break
        if a < min:
            min = a
        if a > max:
            max = a
            
    return min, max
    
def minmax2(lista):
    liczba = lista[0]
    min = liczba
    max = liczba
        
    for liczba in(lista):
        if liczba < min:
            min = liczba
        if liczba > max:
            max = liczba
            
    return min, max
    

def main(args):
    #min, max = minmax1()
    
    #print("Najmniejsza wprowadzona liczba: ", min)
    #print("Największa wprowadzona liczba: ", max)
    
    
    lista = []
    for i in range(100):
        lista.append(random.randint(1, 100))
    print(lista)
    
    min, max = minmax2(lista)
    
    print("Najmniejsza wprowadzona liczba: ", min)
    print("Największa wprowadzona liczba: ", max)
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
