/*
 * liczby2_3.cpp
 * 
 * Copyright 2018  <>
 */


#include <iostream>
#include <iomanip>
using namespace std;

int liczby2() {
    int ile = 0;
    
    for (int i = 1; i < 10; i++){
        for (int j = 0; j < 10; j++){
            if (i != j) {
            cout << i << j << " ";
            ile++;
            }
            }
            
            cout << endl;
            
        }
    return ile;
}

int liczby3() {
    
    
    }
    

int main(int argc, char **argv)
{
    int ile = liczby2();
	cout << "\n\nLiczb 2-cyfrowych: " << ile << endl;
	return 0;
}

