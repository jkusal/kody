/*
 * tekst.cpp
 * 
 * Copyright 2018  <> 
 */


#include <iostream>

using namespace std;

void licz_znaki(char tab[])
{
    int i = 0;
    int biale = 0;
    while(tab[i] != '\0') {
        if(tab[i] == ' ' || tab[i] == '\t') 
            biale++;
        else
            cout << tab[i];
            i++;
        }
    cout << "\nZnaków białych: " << biale << endl;
}

int main(int argc, char **argv)
{
    const int rozmiar = 20;
	char znaki[rozmiar];  // deklaracja tablicy znakowej
    cout << "Jak się nazywasz " ;
    cin.getline(znaki, rozmiar);
    cout << "Cześć "  << znaki << endl;
    licz_znaki(znaki);
    
	return 0;
}

