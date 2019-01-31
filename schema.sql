DROP TABLE IF EXISTS products;

CREATE TABLE products (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT UNIQUE NOT NULL,
      price FLOAT NOT NULL
);

