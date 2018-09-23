DROP TABLE IF EXISTS zamowienia;
CREATE TABLE zamowienia 
(
    NumerZamowienia INTEGER PRIMARY KEY AUTOINCREMENT,
    IDKlient INTEGER,
    DataZamowienia DATE-TIME(25),
    WartZamNetto DECIMAL,
    WartZamBrutto DECIMAL,
    Vat % DECIMAL
);

DROP TABLE IF EXISTS klient;
CREATE TABLE klient
(
	IDKlient INTEGER PRIMARY KEY AUTOINCREMENT,
	NazwaKlienta Text(20),
	Adres TEXT(10),
	Data_aktualizacji DATE(15),
    id_miasta INTEGER(3),
	FOREIGN KEY (id_miasta) REFERENCES miasta(id_miasta)
);

DROP TABLE IF EXISTS dane_gus;
CREATE TABLE dane_gus
(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	Liczba_mieszkancow INTEGER(10),
	Liczba_kobiet INTEGER(10),
	Grupa_wiekowa TEXT(15),
    Data_aktualizacji DATE(15),
    id_miasta INTEGER(3),
    FOREIGN KEY (id_miasta) REFERENCES miasta(id_miasta)
);

