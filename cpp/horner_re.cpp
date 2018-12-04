/*
 * horner_re.cpp
 * 
 * Copyright 2018  <> 
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

float horner_re(int st, float tb[], float x) {
    if (st == 0) return tb[0];
    return horner_re(st-1, tb, x) * x + tb[st];
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
    
    cout << "Wartość wielomianu o postaci: ";
    drukuj(stopien, tb);
    cout << "\ndla x = " << x << " wynosi: " << horner_re(stopien, tb, x);
    cout << endl;
      
	return 0;
}

