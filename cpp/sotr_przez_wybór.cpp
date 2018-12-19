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
    int k;
    for (int i = 0; i < n; i++) {
        k = i;
        for (int j = i + 1; j < n; j++) {
            if (tab[j] < tab[k]) {
                k = j;
            }
        }
        cout << tab[k];
    }
    return 0;
}

int main(int argc, char **argv)
{
    int rozmiar = 20;
    int tablica[rozmiar];  // statyczna deklaracja tablicy
    los(tablica, rozmiar);
    drukuj(tablica, rozmiar);
    cout << endl;
    sort(tablica, rozmiar);
    
	return 0;
}

