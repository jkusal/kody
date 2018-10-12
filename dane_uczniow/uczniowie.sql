DROP TABLE IF EXISTS nazwiska;
CREATE TABLE nazwiska 
(
    id_ucznia INTEGER PRIMARY KEY,
    Nazwisko TEXT(30),
    Pierwsze_imie TEXT(20),
    Drugie_imie TEXT
    
);

DROP TABLE IF EXISTS dane_osobowe;
CREATE TABLE dane_osobowe
(
    id_ucznia INTEGER,
	Dzien_urodzenia NOT NULL,
	Miesiac_urodzenia NOT NULL,
	Rok_urodzenia INTEGER PRIMARY KEY,
    Miejsce_urodzenia TEXT,
	FOREIGN KEY (id_ucznia) REFERENCES nazwiska(id_ucznia)
);

DROP TABLE IF EXISTS oceny;
CREATE TABLE oceny
(
    id_ucznia INTEGER
	Zachowanie DECIMAL DEFAULT NULL,
	Religia_etyka DECIMAL DEFAULT NULL,
	Jezyk_polski DECIMAL DEFAULT NULL,
    Jezyk_angielski DECIMAL DEFAULT NULL,
    Jezyk_niemiecki DECIMAL DEFAULT NULL,
    Matematyka DECIMAL DEFAULT NULL,
    Historia DECIMAL DEFAULT NULL,
    Geografia DECIMAL DEFAULT NULL,
    Biologia DECIMAL DEFAULT NULL,
    Fizyka DECIMAL DEFAULT NULL,
    Chemia DECIMAL DEFAULT NULL,
    Technika DECIMAL DEFAULT NULL,
    Informatyka DECIMAL DEFAULT NULL,
    Plastyka DECIMAL DEFAULT NULL,
    PO DECIMAL DEFAULT NULL,
    W-F TEXT,
	FOREIGN KEY (id_ucznia) REFERENCES nazwiska(id_ucznia)
);
