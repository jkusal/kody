#!/usr/bin/env python
# -*- coding: utf-8 -*-
 


def main(args):
    
    a = int(input("Podaj bok a: ")) 
    i = 0
    
    while i < a:
        a = a - 1
        print("*", end='')
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
