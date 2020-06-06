DROP TABLE IF EXISTS pingshuiyun;
CREATE TABLE pingshuiyun (
    hanzi text,
    sheng integer,
    yunbu text,
    pingz integrer
);

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
	txt text,
	flg text,
	order_num integer,
	zishu integer,
	pingze text,
	yunbu text
);

