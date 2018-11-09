DROP TABLE IF EXISTS pracownicy;
CREATE TABLE pracownicy
(
    id_pracownika INTEGER PRIMARY KEY,
    imię TEXT,
    nazwisko TEXT,
    kod DECIMAL,
    miasto_z TEXT,
    ulica BOOLEAN,
    data_u DATE,
    miasto_u TEXT
);

DROP TABLE IF EXISTS kontakt;
CREATE TABLE kontakt
(
    id_pracownika INTEGER PRIMARY KEY AUTOINCREMENT, 
    typ_k BOOLEAN,
    kontakt DECIMAL,
    uwagi TEXT,
    FOREIGN KEY (id_pracownika) REFERENCES pracownicy(id_pracownika)
);

DROP TABLE IF EXISTS place;
CREATE TABLE place
(
    id_p INTEGER,
    id_s INTEGER PRIMARY KEY,
    placa INTEGER,
    data_z DATE,
    FOREIGN KEY (id_p) REFERENCES pracownicy(id_pracownika),
    FOREIGN KEY (id_s) REFERENCES stanowiska(id_stanowiska)
);



DROP TABLE IF EXISTS stanowiska;
CREATE TABLE stanowiska
(
    id_stanowiska INTEGER PRIMARY KEY,
    stanowisko TEXT
);
