/*
 * wyszukaj.cpp
 * 
 * Copyright 2019  <>
 */


#include <iostream>

using namespace std;

void wypelnij_losowe(int tab[], int roz)
{   
    srand(time(NULL));  // inicjacja generatora pseudolosowych

    for (int i = 0; i < roz; i++)
    {
        tab[i] = rand() % 101;  
    }
}

void drukuj(int tab[], int roz)
{    
    for (int i = 0; i < roz; i++)
    {
        cout << tab[i] << ' ';
    }
}

void insert_sort(int tab[], int n)
{
    cout << "\nSortowanie przez wstawianie:\n";

    int i, j, tmp;

    for(i = 1; i < n; i++)
    {
        tmp = tab[i];
        j = i - 1;
        while (j >= 0 && tab[j] > tmp)
        {
            tab[j+1] = tab[j];
            j--;
        }
        tab[j+1] = tmp;
    }
}

int szukaj_bin_it(int tab[], int n, int szuk)
{
    int p, k, s;
    p = 0, k = n - 1;

    while (p <= k)
    {
        s = (p + k) / 2;
        if (tab[s] == szuk) return s;
        else if (szuk < tab[s]) k = s - 1;
        else p = s + 1;
    }
    return -1;

}

int szukaj_bin_rek(int tab[], int szuk, int p, int k) {
    if (p <= k) {
        int s = (p+k) / 2;
        if (tab[s] == szuk) return s;
        if (szuk < tab[s]) szukaj_bin_rek(tab, szuk, p, s-1);
        else szukaj_bin_rek(tab, szuk, s+1, k);
    }
    return -1;
} 

int main(int argc, char **argv)
{
    int n = 20;
    int tab[n];

    wypelnij_losowe(tab, n);
    drukuj(tab, n);

    int szuk = 0;

    cout << "\nPodaj liczbę: ";
    cin >> szuk;
    insert_sort(tab, n);
    drukuj(tab, n);

    int indeks = szukaj_bin_rek(tab, szuk, 0, n-1);

    if (indeks >= 0)
        cout<< "\nZnaleziona na indeksie " << indeks << endl;
    else
        cout << "\nNie znaleziona! " << endl;
}




