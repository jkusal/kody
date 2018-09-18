
def main(args):
    a = int(input("Podaj a: "))
    print(a)
    
    b = int(input("Podaj b: "))
    print(b)
    
    if a > b:
        print(a, "jest większe od", b)
        
    if a < b:
        print(b, "jest większe od", a)
    
    if a == b:
        print(a, "jest równe", b)
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
