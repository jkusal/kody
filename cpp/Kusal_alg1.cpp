/*
 * Kusal_alg1.cpp
 * 
 * Copyright 2019  <>
 */


#include <iostream>
#include <string.h>

using namespace std;

int main(int argc, char **argv)
{
	int a;
    int i;
    cout << "Podaj liczbę: ";
    cin >> a;
    if (0 < a && a < 100) {
        i = 2;
        if (a == i) 
            cout << a << " jest liczbą parzystą";
        else {
            i = i + 2;
            if (i == 100) {
                cout << a << " nie jest liczbą parzystą";
            }
        }
    }
	return 0;
}

