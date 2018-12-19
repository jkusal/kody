/*
 * bez nazwy.cx
 * 
 * Copyright 2018  <>
 */


#include <iostream>
#include <cstdlib>

using namespace std;

void los(int tab[], int rozmiar)
{
    srand(time(NULL)); //inicjacja generatoraliczb pseudolosowych
    for(int i = 0; i < rozmiar; i++)
    {
        tab[i] = rand() % 101;
    }
}

void drukuj(int tab[], int rozmiar)
{
    for(int i = 0; i < rozmiar; i++)
    {
        cout << tab[i] << ' ';
    }
}

int sort(int tab[], int n) {
    int i = 0;
    for (i; i < n; i++) {
        k = i;
        for (int j = i + 1; j < n; j++) {
            if
            tab[i] = tab[k];
        }
        cout << tab[];
    }
    return 0;
}

int main(int argc, char **argv)
{
    int tablica[rozmiar];  // statyczna deklaracja tablicy
    los(tablica, rozmiar);
    drukuj(tablica, rozmiar);
    sort(tablica, rozmiar);
    
	return 0;
}

