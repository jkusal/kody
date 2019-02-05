/*
 * dec2bin.cpp
 * 
 * Copyright 2019  <>
 */


#include <iostream>
using namespace std;

void dec2any(int liczba, int podstawa, int tab[]) {
    int i=0;
    do {
        tab[i] = liczba % podstawa;
        liczba = liczba / podstawa;
        i++
    } while (liczba != 0);
    return i - 1;
}

void bin2dec(int tab[]) {
    ;
}

int main(int argc, char **argv)
{
    int tab[8];
    int liczna, podstawa;
    cout << "Podaj liczbę i podstawę systemu docelowego: ";
    cin >> liczba >> podstawa;
    int i = dec2any(liczba, podstawa, tab[]);
    cout << "Wynik: "
    petla wyswietla liczbe po konwersji
	return 0;
}

