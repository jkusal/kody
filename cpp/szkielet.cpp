/*
 * szkielet.cpp
 */

#include <iostream>  //biblioteka wejścia/wyjścia

using namespace std;

int main(int /*INTIGER*/ argc, char **argv)
{
	int liczba;   //deklaracja zmiennej typu całkowitego
    liczba = 753;
    std::cout << liczba;  //f8 f9 f5
    
    int a, b, c;  //deklaracja
    a = b = c = d = 0;  //inicjalizacja
    a = 5;
    b = 2 * a;
    c = b - a; 
    d = a/b;
    
    cout << "\n" << a << " " << b << " " << (b - a);
    
	return 0;
}

