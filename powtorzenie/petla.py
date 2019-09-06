#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  petla.py
#  
#  Copyright 2019  <>  
#  
import random

def main(args):
    
    lista = []
    for i in range(5):
        lista.append(random.randint(1, 30))
    print(lista)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
