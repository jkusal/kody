#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main(args):
    
    a = 10
    b = 100
		
    if a <= b:
        for liczba in range(a, b):
			if liczba % 3 == 0:
                print(liczba)
   
         
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
