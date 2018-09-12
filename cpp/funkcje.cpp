/*
 * szablon.cpp
 * 
 * Copyright 2018  <>
 * 
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * 
 * 
 */


#include <iostream>

using namespace std;

int suma(int a, int b){
    
    return a + b;
    
    }
    
int roznica(int a, int b){
    
    return a - b;
    
    }
    
int iloczyn(int a, int b){
    
    return a * b;
    
    }
    
int iloraz(int a, int b){
    
    return a / b;
    
    }

int main(int argc, char **argv)
{ /* DRY - Don't repat yourself */
	
    int a, b;
    
    a = b = 0;
    
    cout << "Podaj liczbę: ";
    cin >> a;
    
    cout << endl << "Podaj drugą liczbę: ";
    cin >> b;
    
    cout << a << "," << b;
    
    cout << endl << "suma: "; 
    cout << suma(a, b);
    
    cout << endl << "różnica: ";
    cout << roznica(a, b);
    
    cout << endl << "iloczyn: ";
    cout << iloczyn(a, b);
    
    cout << endl << "iloraz: ";
    cout << iloraz(a, b);
    
    
    
	return 0;
}

