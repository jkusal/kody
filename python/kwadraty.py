#!/usr/bin/env python
# -*- coding: utf-8 -*-  

import turtle

def rysujKwadrat(zolw, bok):
    for i in range(4):
        zolw.forward(bok)
        zolw.right(90)
    
def main(args):
    turtle.title("Kwadraty")
    turtle.setup(1000, 800)
    
    zolw = turtle.Turtle()
    zolw.color('green')
    
    rysujKwadrat(zolw, 100)
    
    turtle.done()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
