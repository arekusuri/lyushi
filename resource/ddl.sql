CREATE TABLE IF NOT EXISTS poetry (
	pid text PRIMARY KEY,
	author text NOT NULL,
	dynasty text NOT NULL,
	title text,
	tiba text,
	category int
);

CREATE TABLE IF NOT EXISTS half (
	pid text,
	num integrer,
	txt text,
	flg text
);
