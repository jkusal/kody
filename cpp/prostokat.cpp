
#include <iostream>
#include <cmath>  /* podpięcie biblioteki matematycznej */

using namespace std;

int pole(int a, int b){
    
    return a * b;
    
    }
    
int obwod(int a, int b){
    
    return a + a + b + b;
    
    } 
      
int main(int argc, char **argv)
{
    int a, b;
    
    a = b = 0;
    
    cout << "Podaj wysokość prostokąta: ";
    cin >> a;
    
    cout << endl << "Podaj szerokość prostokąta: ";
    cin >> b;
    
    cout << a << "x" << b;
    
    cout << endl << "pole: "; 
    cout << pole(a, b);
    
    cout << endl << "obwód: ";
    cout << obwod(a, b);
	
	return 0;
}

