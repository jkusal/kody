/*
 * euklides.cpp
 * 
 * Copyright 2018  <> 
 */


#include <iostream>
#include <iomanip>
using namespace std;

int euklides(int a, int b) {
    int licznik = 0;
    while(a > 0){
        a = a % b;
        b = b - a;
        licznik += 1;
    }
    cout << "Powtorzeń: " << licznik << endl;
    return b;    
}

int nwd_klasyczny(int a, int b) {

    int licznik = 0;
    while(a != b){
        if (a > b) {
            a -= b;
            licznik += 1;
            }
        else {
            b -= a;
            licznik += 1;
            }
        }
    cout << "Powtorzeń: " << licznik << endl;
    return b;    
}

int main(int argc, char **argv)
{
	int a, b; //deklaracja
    a = b = 0; //inicjacja
    cout << "Podaj liczbę pierwszą: ";
    cin >> a;
    cout << "Podaj liczbę drugą: ";
    cin >> b;
    cout << nwd_klasyczny(a, b) << endl;
    cout << euklides(a, b);
	return 0;
}

