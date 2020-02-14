CREATE TABLE `sito` (
	`Link`	TEXT NOT NULL,
	`Nome`	TEXT,
	PRIMARY KEY(Link)
);

CREATE TABLE `prodotto` (
	`ID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`Nome`	TEXT,
	`Prezzo`	NUMERIC,
	`Tipologia`	TEXT,
	`Sito`	TEXT NOT NULL
);

CREATE TABLE `linkScraper` (
	`link`	TEXT NOT NULL,
	`sito`	TEXT NOT NULL,
	PRIMARY KEY(link)
);
