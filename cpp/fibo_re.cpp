/*
 * fibo_re.cpp
 * 
 * Copyright 2018  <> 
 */


#include <iostream>
using namespace std;

int vibo_re(int n) 
{
    if (n == 0) return 0;
    if (n == 1) return 1;
    return vibo_re(n-2) + vibo_re(n-1);
}

int main(int argc, char **argv)
{
	int n;
    cout << "Podaj numer wyrazu ciągu: ";
    cin >> n;
    cout << "Ciąg Fibonacciego do wyrazu " << n << ": ";
    cout << vibo_re(n) << endl;
    
    for (int i = 0; i <= n; i++) {
        cout << vibo_re(i) << endl;
        if (i < 2) continue;
        else {
            cout << (float)vibo_re(i) / (float)vibo_re(i-1) << endl;
        }
    }
    
	return 0;
}

