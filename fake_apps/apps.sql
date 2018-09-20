DROP TABLE IF EXISTS fake_apps;
CREATE TABLE fake_apps (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT DEFAULT '',
    downloads INTEGER,
    price DECIMAL
);