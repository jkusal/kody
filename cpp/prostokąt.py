
def pole(a, b):
    return a * b
    
def obwod(a, b):
    return a + a + b + b

def main(args):
    a = int(input("Podaj wysokość: "))
    print(a)
    
    b = int(input("Podaj szerokość: "))
    print(b)
    
    print("Pole: ", pole(a, b))
    
    print("Obwód: ", obwod(a, b))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
