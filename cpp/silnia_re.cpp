/*
 * silnia_re.cpp
 * 
 * Copyright 2018  <> 
 */


#include <iostream>
using namespace std;

float silnia_re(int n)
{
    if (n == 0) return 1;
    return silnia_re(n-1) * n;
}

int main(int argc, char **argv)
{
    int n;
    cout << "Podaj liczbę: "; cin >> n;
    cout << "Wynik: " << silnia_re(n);
	return 0;
}
