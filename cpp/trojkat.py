# 


def trojkat(a, b, c):
    """
    Funkcja przyjmuje trzy liczby - długości boków trójkąta
    Funkcja sprawdza, czy da się z nich zbudować trójkąt
    Funkcja zwraca True jeśli się da, False w przeciwnym razie
    """
    
    wynik = False
    
    if a + b > c and a + c > b and b + c > a:
        wynik = True
    
    return wynik


def main(args):
    assert(trojkat(4, 7, 5) == True)
    assert(trojkat(9, 3, 5) == False)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
