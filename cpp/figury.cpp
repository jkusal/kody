/*
 * figury.cpp
 * 
 * Copyright 2018  <>
 */


#include <iostream>
#include <iomanip>
using namespace std;

void prostokat(int a, int b, char z) {
    for (int i = 0; i < a; i++) { 
        for (int j = 0; j < b; j++)
            if (j == 0 || j == b - 1 || i == 0 || i == a - 1)
                cout << z;
            else
                cout << " ";
        cout << endl;
        }
    }

int main(int argc, char **argv)
{
	int a, b; //deklaracja
    a = b = 0; //inicjacja
    cout << "Podaj bok a: ";
    cin >> a;
    cout << "Podaj bok b: ";
    cin >> b;
    char znak;
    cout << "Podaj znak: ";
    cin >> znak;
    
    prostokat(a, b, znak);
	return 0;
}

