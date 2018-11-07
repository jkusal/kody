/*
 * palidrom.cpp
 * 
 * Copyright 2018  <> 
 * funkcja pobiera tablicę i ilość znaków
 */
// funkcja sprawdz czy liczba jest palindromem 

#include <iostream>
#include <string.h>
using namespace std;

bool palindrom(char tb[], int roz) {
        int i;
        int a = roz  / 2;
        bool czyPal = true;
        for(i = 0; i < a; i++) {
            if(tb[i] == tb[roz - 1 - i]);
            else {
                czyPal = false;
                break;
        }
    }
    return czyPal;
}

bool liczba(char tb[], int roz) {
        
}

int main(int argc, char **argv)
{
    const int rozmiar = 50;
    char tb[rozmiar];
    cout << "Podaj wyraz: ";
    cin.getline(tb, rozmiar);
    if(palindrom(tb, strlen(tb)))
        cout << "Palindrom!";
    else
        cout << "The thing";
	
	
    return 0;
}

