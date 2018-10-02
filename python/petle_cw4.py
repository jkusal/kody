#!/usr/bin/env python
# -*- coding: utf-8 -*-



def main(args):
	
	for a in range(10, 100):
		if a %2 ==0 and a %3 == 0:
			print (a)

if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
