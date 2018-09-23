#
#Program pobiera 3 liczby od użytkownika , a następnie wyświetla największą
#
def maks(a, b, c):
<<<<<<< HEAD
    m=None
    
    if a >= b & a >= c:
        print(a, "jest największe")
    elif b >= a & b >= c:
        print(b, "jest największe")
    else: 
        print(c, "jest największe")
        
    return m;
=======
    if a > b:
        if a > c:
            m = a
        else:
			m = c 
    elif b > c:
            m = b
    print("Największa:", m)
    
return m
    
def maks2(a, b, c):
    m = a
    if b > m:
        m = b
    if c > m:
        m = c
    return m
>>>>>>> 9de830c13c220ff050a11f1ca3fccf701744ae5f



def main(args):
    assert(maks(3, 2, 1) == 3)
    assert(maks(1, 3, 1) == 3)
    assert(maks(1, 2, 3) == 3)
    assert(maks(1, 1, 3) == 3)
    assert(maks(3, 1, 1) == 3)
    assert(maks(3, 3, 1) == 3)
    assert(maks(1, 3, 3) == 3)
    assert(maks(3, 3, 3) == 3)
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
