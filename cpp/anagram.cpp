/*
 * anagram.cpp
 * 
 * Copyright 2018  <> 
 */
// anagram - odwraca znaki w jednym wyrazie
// wyrazy - funkcja dzieli tekst na wyrazy

#include <iostream>
using namespace std;

int zlicz(char tab[]) {
    int i = 0;
    while(tab[i] != '\0') i++;
    return i;
}

void wyswietl(char tekst[], int roz) {
    for(int i = 0; i < roz; i++) {
        cout << tekst[i];
        }
}


void anagram(char tab[], roz) {
    int i = 0;
    for(i = roz - 1, i >= 0; i--) {
            
        }
}


int main(int argc, char **argv)
{
    const int roz = 50;
	char tekst[roz];  
    cout << "Podaj jeden wyraz " ;
    cin.getline(tekst, roz);
    cout << "Wyraz: "  << tekst << endl;
    wyswietl(tekst, zlicz(tekst));
    
	return 0;
}

