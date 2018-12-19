/*
 * lpierwsza.cpp
 * 
 * Copyright 2018  <> 
 */


#include <iostream>

int main(int argc, char **argv)
{
	int n;
    cout << "Podaj n: ";
    cin >> n;
    for (int i = 2; i*i <= n; i++) {
        if (n % i = 0) {
            cout << "Złożona";
            return 0;
        }
    }
    cout << "Pierwsza";
    
	return 0;
}

