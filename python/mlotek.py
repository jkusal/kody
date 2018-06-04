#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

# ctrl shift P


def main(args):
    liczba = random.randint(1, 10)
    #  print("Wylosowano:", liczba)
    for i in range(3):
        odp = input("Podaj liczbę od 1 do 10: ")
        print("Podaleś liczbę:", odp)

        if liczba == int(odp):
            print("Zgadłeś!")
        else:
            print("Spróbuj jeszcze raz!")

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
