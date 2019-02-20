/*
 * szyfr_cezara.cpp
 * 
 * Copyright 2019  <> 
 */


#include <iostream>
#include <string.h>
using namespace std;

#define MAKS 100

void szyfruj(char tekst[], int klucz)
{
    int ilosc = strlen(tekst);
    cout << ilosc << endl;
    int reszta = ilosc % klucz;
    if(reszta > 0) {
        for(int i = ilosc; i < ilosc + klucz - reszta; i++) {
            tb[i] = '.';
            int kod = (int)tekst[i];
            kod += klucz;
        }
    }
}


int main(int argc, char **argv)
{    
    char tekst[MAKS];
    int klucz = 0;
    
    cout << "Wprowadź tekst do szyfrowania: ";
    cin.getline(tekst, MAKS);
    cout << strlen(tekst) << endl;
    
    cout << "Podaj klucz: ";
    cin >> klucz;
    
    szyfruj(tekst,klucz);
	
	return 0;
}


