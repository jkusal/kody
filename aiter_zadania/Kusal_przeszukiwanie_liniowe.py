#!/usr/bin/env python
# -*- coding: utf-8 -*-  

import random

def main(args):
    tab[n] = 0
    szuk = []
    for j in range(10):
        szuk.append(random.randint(0, 50))
    print (szuk)
    i = 0
    tab[n] = szuk
    for i in range(szuk + 1):
        if tab[i] == szuk:
            i = i + 1
        else:
            if i < n:
                print("Element znaleziony")
                return
            else:
                print("Element nieznaleziony")
                return
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
