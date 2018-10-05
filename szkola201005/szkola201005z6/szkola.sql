DROP TABLE IF EXISTS oceny;
CREATE TABLE oceny 
(
    ID_ucznia INTEGER PRIMARY KEY,
    Ocena INTEGER,
    data DATA,
    ID_przedmiotu INTEGER,
    FOREIGN KEY (ID_przedmiotu) REFERENCES przedmioty(ID_przedmiotu)
);

DROP TABLE IF EXISTS przedmioty;
CREATE TABLE przedmioty
(
	ID_przedmiotu INTEGER PRIMARY KEY,
	Nazwa_przedmiotu TEXT,
	Nazwisko_nauczyciela NOT NULL,
    Imie_nauczyciela NOT NULL
);

DROP TABLE IF EXISTS uczniowie;
CREATE TABLE uczniowie
(
	ID_ucznia INTEGER,
	nazwisko TEXT,
	Imie TEXT,
    Ulica TEXT,
    Dom INTEGER,
    ID_klasy INTEGER,
	FOREIGN KEY (ID_ucznia) REFERENCES oceny(ID_ucznia)
);

