/*
 * palindrom_2.cpp
 * 
 * Copyright 2018  <>
 */


#include <iostream>
#include <string.h>

using namespace std;

bool palindrom(char liczba[], int rozmiar)
{
    int polowa = rozmiar / 2;
    bool czyPal = true;
    
    for(int i = 0; i < polowa; i++)
    {
        if (liczba[i] == liczba[rozmiar - 1 - i])
            ; // instrukcja pusta
        else
        {
            czyPal = false;
            break;
        }
    }
    
    return czyPal;
}

int main(int argc, char **argv)
{
    const int rozmiar = 50;
    char liczba[rozmiar];
    cout << "Podaj liczbę: ";
    cin.getline(liczba, rozmiar);
	
    // cin.gcount wlicza w długość sekwencję /0 więc dolicza dodatkowy znak
    //if (palindrom(tekst, cin.gcount()-1))  lub przez dołączenie biblioteki string:
    if (palindrom(liczba, strlen(liczba)))
        cout << "Palindrom! :)";
    
    else
    {
        cout << "To nie palindrom :(";
    }
    
    
	return 0;
}

