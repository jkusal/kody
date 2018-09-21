DROP TABLE IF EXISTS miasta;
CREATE TABLE miasta 
(
    id_miasta INTEGER PRIMARY KEY AUTOINCREMENT,
    Nazwa_miasta TEXT(30),
    Wojewodztwo TEXT(20)
    
);

DROP TABLE IF EXISTS powierzchnie;
CREATE TABLE powierzchnie
(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	Powierzchnia_miasta DECIMAL(10),
	Powierzchnia_terenow_zielonych DECIMAL(10),
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
