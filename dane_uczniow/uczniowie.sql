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
	Dzien_urodzenia NOT NULL,
	Miesiac_urodzenia NOT NULL,
	Rok_urodzenia INTEGER PRIMARY KEY,
    Miejsce_urodzenia TEXT,
    id_ucznia INTEGER,
	FOREIGN KEY (id_ucznia) REFERENCES nazwiska(id_ucznia)
);

DROP TABLE IF EXISTS oceny;
CREATE TABLE oceny
(
	Zachowanie INTEGER,
	Religia_etyka INTEGER,
	Jezyk_polski INTEGER,
    Jezyk_angielski INTEGER,
    Jezyk_niemiecki INTEGER,
    Matematyka INTEGER,
    Historia INTEGER,
    Geografia INTEGER,
    Biologia INTEGER,
    Fizyka INTEGER,
    Chemia INTEGER,
    Technika INTEGER,
    Informatyka INTEGER,
    Plastyka INTEGER,
    PO INTEGER,
    W-F INTEGER,
    id_ucznia INTEGER,
	FOREIGN KEY (id_ucznia) REFERENCES nazwiska(id_ucznia)
);
