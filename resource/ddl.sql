CREATE TABLE IF NOT EXISTS info (
	pid text PRIMARY KEY,
	poet text NOT NULL,
	dynasty text NOT NULL,
	title text,
	category int
);

CREATE TABLE IF NOT EXISTS half (
	pid text PRIMARY KEY,
	num integrer,
	txt text
);
