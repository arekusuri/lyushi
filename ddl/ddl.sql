DROP TABLE IF EXISTS poetry;
CREATE TABLE poetry (
	pid text PRIMARY KEY,
	author text NOT NULL,
	dynasty text NOT NULL,
	title text,
	tiba text,
	category int
);

DROP TABLE IF EXISTS half;
CREATE TABLE half (
	pid text,
	num integrer,
	txt text,
	flg text
);

DROP TABLE IF EXISTS pingshuiyun;
CREATE TABLE pingshuiyun (
    hanzi text,
    sheng integrer,
    yunbu text,
    pingz integrer
)