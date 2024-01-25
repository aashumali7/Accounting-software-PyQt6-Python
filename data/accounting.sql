CREATE TABLE IF NOT EXISTS users (
    id   INTEGER PRIMARY KEY,
    username TEXT NOT NULL COLLATE NOCASE,
    password TEXT NOT NULL COLLATE NOCASE,
    role TEXT CHECK(role IN ('businessowner', 'accountant', 'operator'))
);

CREATE TABLE IF NOT EXISTS customers (
    id   INTEGER PRIMARY KEY,
    name TEXT NOT NULL COLLATE NOCASE
);

CREATE TABLE IF NOT EXISTS suppliers (
    id   INTEGER PRIMARY KEY,
    name TEXT NOT NULL COLLATE NOCASE
);

CREATE TABLE IF NOT EXISTS items (
    id   INTEGER PRIMARY KEY,
    name TEXT NOT NULL COLLATE NOCASE
);