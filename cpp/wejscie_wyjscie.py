#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  wejscie_wyjscie.py
#  
#  Copyright 2018  <>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  duck typing jeżeli coś wygląda jak kaczka musi być kaczką
#  wszystko pobrane z wejścia jest znakiem


def main(args):
    a = int(input("Podaj liczbę: "))
    print(a)
    
    b = int(input("Podaj drugą liczbę: "))
    print(b)
    
    print("Suma: ", a + b)
    
    print("Iloczyn: ", a * b)
    
    print("Iloraz: ", a / b)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
