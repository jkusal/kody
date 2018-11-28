/*
 * fibonacci.cpp
 * 
 * Copyright 2018  <>
 */


#include <iostream>
using namespace std;

int vibo_it(int n) {
    int a = 0;
    int b = 1;
    int wynik = 0;
    if (n < 1) return a;
    else if (n < 2) return b;
    for(int i = 2; i <= n; i++) {
        wynik = a + b;
        a = b;
        b = wynik;
    }
    return wynik;
}

int main(int argc, char **argv)
{
	float n;
    cout << "Podaj numer wyrazu ciągu: ";
    cin >> n;
    cout << "Ciąg Fibonacciego do wyrazu " << n << ": ";
    cout << vibo_it(n) << endl;
    
    for (int i = 0; i <= n; i++) {
        cout << vibo_it(i) << endl;
    }
    
    cout << "Złota liczba: " << vibo_it(n -1)/vibo_it(n - 2);
    
    
	return 0;
}

