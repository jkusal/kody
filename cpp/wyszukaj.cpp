/*
 * wyszukaj.cpp
 * 
 * Copyright 2019  <>
 */


#include <iostream>
#include <cstdlib>

using namespace std;

void los(int tab[], int rozmiar)
{
    srand(time(NULL));  // inicjacja generatoraliczb pseudolosowych
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

void sort_insert(int tab[], int n)
{
    cout << "\nSortowanie przez wstawianie" << endl;
    int i, j, tmp;
    for(i = 1; i < n; i++)  // pętla wybiera elementy zaczynając od drugiego
    {
        tmp = tab[i];
        j = i - 1;
        while(j >= 0 && tab[j] >tmp)
        {
            tab[j+1] = tab[j];
            j--;
        }
        tab[j+1] = tmp;
    }
}

int szukaj_bin_it(int tab[], int n, int szuk) {
    int p, k, s;
    p = 0; k = n - 1;
    while (p <= k){
        s = (p + k) / 2;
        if (tab[s] == szuk) return s;
        else if (szuk < tab[s]) k = s - 1;
        else p = s +1;
    }
}

int main(int argc, char **argv)
{
	int rozmiar = 10;
    int tablica[rozmiar];  // statyczna deklaracja tablicy
    int szuk = 0;
    los(tablica, rozmiar);
    drukuj(tablica, rozmiar);
    cout << endl;
    sort_insert(tablica, rozmiar);
    drukuj(tablica, rozmiar);
    
    cout << "Podaj liczbę: ";
    cin >> szuk;
    
    int indeks = szukaj_bin_it(tablica, rozmiar, szuk);
    
    if  (indeks >= 0)
        cout << "\nZnaleziona na indeksie: " << indeks << endl;
    else
        cout << "\nNie znaleziona! " << indeks << endl;
        
	return 0;
}

