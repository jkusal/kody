#!/usr/bin/env python
# -*- coding: utf-8 -*-
  
import sqlite3

def kwerenda1(cur):
    cur.execute("""
    WITH srednie AS (
        SELECT imie, nazwisko, AVG(ocena) AS poile FROM uczniowie INNER JOIN oceny ON uczniowie.id=oceny.id_uczen GROUP BY uczniowie.id )
        SELECT nazwisko, imie, poile FROM srednie
        WHERE poile >= 4.0
    """)
    
    wyniki = cur.fetchall()
    for row in wyniki:
        print(row)

# SELECT * FROM uczniowie WHERE nazwisko LIKE 'G%'
# SELECT * FROM uczniowie WHERE nazwisko='Piasecki'
# SELECT * FROM uczniowie WHERE nazwisko='Piasecki' AND imie='Rafał'
# SELECT egz_hum, egz_mat FROM uczniowie WHERE nazwisko='Piasecki' AND imie='Rafał'
# SELECT nazwisko, imie, egz_hum, egz_mat FROM uczniowie ORDER BY egz_hum DESC 
# SELECT nazwisko, imie, egz_hum, egz_mat FROM uczniowie ORDER BY egz_hum DESC LIMIT 5
# SELECT nazwisko, imie, egz_hum, egz_mat FROM uczniowie WHERE /imie LIKE '%a'/plec=1
# SELECT nazwisko, imie, egz_hum, egz_mat FROM uczniowie WHERE egz_hum > 40 AND egz_mat > 40 ORDER BY nazwisko ASC 
# SELECT COUNT(*) FROM klasy INNER JOIN uczniowie ON klasy.id=uczniowie.id_klasa WHERE klasa='1A'
# SELECT klasa, COUNT(uczniowie.id) FROM klasy INNER JOIN uczniowie ON klasy.id=uczniowie.id_klasa GROUP BY klasa
# SELECT klasa, COUNT(uczniowie.id) AS ile FROM klasy INNER JOIN uczniowie ON klasy.id=uczniowie.id_klasa GROUP BY klasa ORDER BY ile DESC
# SELECT imie, nazwisko, AVG(ocena) FROM oceny INNER JOIN uczniowie ON oceny.id_uczen=uczniowie.idWHERE imie='Dorota' AND nazwisko='Nowak'
# SELECT imie, nazwisko, AVG(ocena) AS poile FROM uczniowie INNER JOIN oceny ON uczniowie.id=oceny.id_uczen GROUP BY uczniowie.id ORDER BY poile DESC
# WITH srednie AS (
        #SELECT imie, nazwisko, AVG(ocena) AS poile FROM uczniowie INNER JOIN oceny ON uczniowie.id=oceny.id_uczen GROUP BY uczniowie.id )
        #SELECT nazwisko, imie, poile FROM srednie
        #WHERE poile >= 4.0


def main(args):
    baza_nazwa = 'baza_prep'
    table = ['uczniowie', 'klasy', 'przedmioty', 'oceny']

    con = sqlite3.connect(baza_nazwa + '.db')  # połączenie z bazą
    cur = con.cursor()  # utworzenie kursora
    
    kwerenda1(cur);
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
