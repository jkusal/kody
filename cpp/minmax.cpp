/*
 * minmax.cpp
 * 
 * Copyright 2018  <> 
 */


#include <iostream>
#include <iomanip>
#include <cstdlib>
using namespace std;

void wypelnij(int tab[], int rozmiar) {
        cout << "Podaj " << rozmiar << " liczb: " << endl;
        for(int i = 0; i < rozmiar; i++) {
                cin >> tab[i];
        }
}

void drukuj(int tab[], int rozmiar) {
        for(int i = 0; i < rozmiar; i++) {
                cout << tab[i] << " ";
        }
}

int min1(int tab[], int roz) {
    int min = tab[0];
    for(int i = 1, i < roz, i++) {
        if(tab[i] < min)
            min = tab[i];
        
    }
    return min;
}

int max1(int tab[], int roz) {
    int min = tab[0];
    for(int i = 1, i < roz, i++) {
        if(tab[i] < min)
            min = tab[i];
        
    }
    return min;
}

void wypelnij_los(int tab[], int rozmiar) {
        srand(time(NULL));  // generator liczb pseudolosowych
        for(int i = 0; i < rozmiar; i++) {
                tab[i] = rand() % 101; 
        }
}


int main(int argc, char **argv)
{
	int rozmiar = 50;
    int tab[rozmiar];
    wypelnij_los(tab, rozmiar);
    drukuj(tab, rozmiar);
	return 0;
}

