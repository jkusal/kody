/*
 * anagram.cpp
 * 
 * Copyright 2018  <> 
 */
// anagram - odwraca znaki w jednym wyrazie
// wyrazy - funkcja dzieli tekst na wyrazy

#include <iostream>
using namespace std;

int zlicz(char tb[])
{
    int i = 0;
    
    while(tb[i] != '\0') i++;
    
    return i;
}

void wyswietl(char tb[], int roz)
{
    for (int i = 0; i < roz; i++)
    {
        cout << tb[i];
    }
}

void anagram(char tb[], int roz)
{
    for (int i = roz - 1; i >= 0; i--) {
        
        cout << tb[i];
    }
}

int main(int argc, char **argv)
{
    const int rozmiar = 50;
    char tekst[rozmiar];
    
    cin.getline(tekst, rozmiar);
    
    wyswietl(tekst, cin.gcount());
    cout << endl;
    anagram(tekst, zlicz(tekst));

    
	return 0;
}

