#
#Program pobiera 3 liczby od użytkownika , a następnie wyświetla największą
#
def maks(a, b, c):
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
