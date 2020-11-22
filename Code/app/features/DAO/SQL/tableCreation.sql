DROP TABLE IF EXISTS Hands CASCADE;
DROP TABLE IF EXISTS Piles CASCADE;
DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS Games CASCADE;
DROP TABLE IF EXISTS Belote CASCADE;
DROP SEQUENCE IF EXISTS idHands_seq;
DROP SEQUENCE IF EXISTS idPile_seq;
DROP SEQUENCE IF EXISTS idUsers_seq;
DROP SEQUENCE IF EXISTS idGame_seq;
DROP SEQUENCE IF EXISTS idBelote_seq;



CREATE SEQUENCE idHands_seq;
CREATE TABLE Hands
(
    idHands integer NOT NULL DEFAULT nextval
    ('idHands_seq'::regclass) PRIMARY KEY,
    listCard text
);


CREATE SEQUENCE idUsers_seq;
CREATE TABLE users
(
    idUsers integer NOT NULL DEFAULT nextval
	('idUsers_seq'::regclass) PRIMARY KEY,
	username text,
    mdp text,
    admini boolean,
    connected boolean,
    score integer
);

CREATE SEQUENCE idPile_seq;
CREATE TABLE Piles
(
    idPile integer NOT NULL DEFAULT nextval
    ('idPile_seq'::regclass) PRIMARY KEY,
    card1 text,
    card2 text,
    card3 text,
    card4 text
);


CREATE SEQUENCE idGame_seq;
CREATE TABLE Games
(
    idGame integer NOT NULL DEFAULT nextval
    ('idGame_seq'::regclass) PRIMARY KEY, 
    jeu text,
    idPlayers text,
    score text
);


CREATE SEQUENCE idBelote_seq;
CREATE TABLE Belote
(
    idBelote integer NOT NULL DEFAULT nextval
    ('idBelote_seq'::regclass) PRIMARY KEY,
    players text,
    handList text, 
    score1 text,
    score2 text,
    atout text, 
    maitre text,
    saved bool,
    finished bool
);
ALTER TABLE Belote
ADD COLUMN idGame integer,
ADD FOREIGN KEY (idGame) REFERENCES Games(idGame);

ALTER TABLE Hands
ADD COLUMN idGame integer,
ADD FOREIGN KEY (idGame) REFERENCES Games(idGame);

ALTER TABLE Hands
ADD COLUMN idUsers integer,
ADD FOREIGN KEY (idUsers) REFERENCES Users(idUsers);

ALTER TABLE Piles
ADD COLUMN idGame integer,
ADD FOREIGN KEY (idGame) REFERENCES Games(idGame);