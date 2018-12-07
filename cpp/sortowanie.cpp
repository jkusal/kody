/*
 * sortowanie.cpp
 */


#include <iostream>
#include <cstdlib>

using namespace std;

void los(int tab[], int rozmiar)
{
    srand(time(NULL)); //inicjacja generatoraliczb pseudolosowych
    for(int i = 0; i < rozmiar; i++)
    {
        tab[i] = rand() % 101;
    }
}

void drukuj(int tab[], int rozmiar)
{
    for(int i = 0; i < rozmiar; i++)
    {
        cout << tab[i] << ' ';
    }
}

//~ void zamien(int &a, int &b)
//~ {
    //~ int tmp; //zmienna pomocnicza
    //~ tmp = a;
    //~ a = b;
    //~ b = tmp;
//~ }

void zamien(int tab[], int i)
{
    int tmp = tab[i];
    tab[i] = tab[i+1];
    tab[i+1] = tmp;
}

void sortowanie_babelkowe+(int tab[],int n)
{
    cout << "\nSortowanie bąbelkowe+" << endl;
    int licz = 0;
    for(int j = n - 1; j > 0; j--)
    {
        for(int i = 0; i <  j; i++) //pętla wewnętrzna
        {
            licz++;
            if(tab[i] > tab[i+1])
            {
                //zamiana miejscami
                zamien(tab, i);
            }
        }
    }
    cout << "Powtórzenia: " << licz << endl;
}

void sortowanie_babelkowe-(int tab[],int n)
{
    cout << "\nSortowanie bąbelkowe+" << endl;
    int licz = 0;
    for(int j = 0; j < n; j++)
    {
        for(int i = 0; i <  j; i--) //pętla wewnętrzna
        {
            licz++;
            if(tab[i] > tab[i+1])
            {
                //zamiana miejscami
                zamien(tab, i);
            }
        }
    }
    cout << "Powtórzenia: " << licz << endl;
}

int main(int argc, char **argv)
{
    int rozmiar =20;
    int tablica[rozmiar];  // statyczna deklaracja tablicy
    los(tablica, rozmiar);
    drukuj(tablica, rozmiar);
    cout << endl;
    sortowanie_babelkowe+(tablica, rozmiar);
    drukuj(tablica, rozmiar);
    sortowanie_babelkowe-(tablica, rozmiar);
    drukuj(tablica, rozmiar);
    
    return 0;
}

