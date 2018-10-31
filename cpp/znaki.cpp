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
    int biale, inter, licz;
    biale = inter = licz = 0;
    while(tab[i] != '\0') {
        //if(tab[i] == ' ' || tab[i] == '\t') 
          //  biale++;
        //else
           // cout << tab[i];
        switch  (tab[i])  {
            case ' ': biale++; break;
            case '\t': biale++; break;
            case ',': inter++; break;
            case '.': inter++; break;
            default: licz++; break;
        }  
        i++;
        }
    cout << "\nZnaków białych: " << biale << endl;
    cout << "\nZnaków interpunkcyjnych: " << inter << endl;
    cout << "\nZnaków innych: " << licz << endl;
}

void ascii(char tab[]) {
    int i = 0;
    while(tab[i] != '\0') {
        cout << (int)tab[i] << " " << endl;
        i++;
    }
} 
// A-Z ascii 65-90
// a-z ascii 97-122
void zamiana_liter(char tab[]) {
    int i = 0;
    int a;
    while(tab[i] != '\0') {
        a = (int)tab[i];
        if(a >= 65 && a <= 90) 
            a += 32;
        else if(a >= 97 && a <= 122)
                a -=32;
            //a = (char)(int)tab[i];
            cout << (char)a;
            i++;
            
        //(int)tab[i]
        //(char)(int)tab[i]
    }
}

int main(int argc, char **argv)
{
    const int rozmiar = 20;
	char znaki[rozmiar];  // deklaracja tablicy znakowej
    cout << "Jak się nazywasz " ;
    cin.getline(znaki, rozmiar);
    cout << "Cześć "  << znaki << endl;
    //licz_znaki(znaki);
    ascii(znaki);
    zamiana_liter(znaki);
    
	return 0;
}

