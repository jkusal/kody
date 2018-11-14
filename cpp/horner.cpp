/*
 * horner.cpp
 * 
 * Copyright 2018  <>
 * 
 * w(x) = 2x^3 + 3x^2 + 5x + 4 => 6 mnożeń + 3 dodawania
 * w(x) = x (2x^2 + 3x + 5) + 4 =>
 * w(x) = x ( x (2x + 3) +5) + 4 =>
 *  
 */


#include <iostream>
using namespace std;

void drukuj(int st, float tb[]) {
    int i = 0;
    for (i = 0; i < st; i++) {
        cout << tb[i] << "x^" << st - i << " + ";
    }
    cout << tb[i] << endl;
}

float horner_it(int st, float tb[], float x) {
    float wynik = tb[0]; 
    for (int i = 1; i <= st; i++) {
        wynik = wynik * x + tb[i]; 
    }
    return wynik;
}

int main(int argc, char **argv)
{
    
    int stopien = 0;
    float x = 0;
    cout << "Podaj stopień wielonianu: ";
    cin >> stopien;  
    float *tb; // wskażnik - zmienna, która przechowuje adres komorki w pamięci 
    tb = new float [stopien+1];
    for (int i = 0; i <= stopien; i++) {
        cout << "Podaj wspołczynnik przy potędze " << stopien - i <<": ";
        cin >> tb[i];
    }
    
    cout << "Podaj argument: ";
    cin >> x;
      
    cout << "Wartość wielomianu o postaci: ";
    drukuj(stopien, tb);
    cout << "\ndla x = " << x << " wynosi: " << horner_it(stopien, tb, x);
    cout << endl;
      
	return 0;
}

