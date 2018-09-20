#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

# ctrl shift P


def main(args):
    ileliczb = int(input("Podaj ilość typowanych liczb: "))
    maksliczba = int(input("Podaj maksymalną losowaną liczbę: "))
    print("Wytypuj {} z {} liczb".format(ileliczb, maksliczba))

    # print("Wylosowano:", liczba)
    # losowanie liczb
    liczby = []  # lista wylosowanych liczb
    i = 0
    # for i in range(ileliczb):
    while i < ileliczb:
        liczba = random.randint(1, maksliczba)
        if liczby.count(liczba) == 0:
            liczby.append(liczba)
            i += 1
    print(liczby)

    typy = set()  # deklaracja pustego zbioruna typy użytkownika
    i = 0
    while i < ileliczb:
        typ = input("Podaj liczbę {}: ".format(i + 1))
        if typ not in typy:
            typy.add(typ)
            i += 1
    print(typy)

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))


   # lista przechowuje podane wartości
