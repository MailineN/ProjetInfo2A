DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS id_users_seq;
CREATE SEQUENCE id_users_seq;
CREATE TABLE users
(
    id_users integer NOT NULL DEFAULT nextval
	('id_users_seq'::regclass) PRIMARY KEY,
	username text,
    mdp text,
    admini boolean,
    connected boolean,
    score integer);

DROP TABLE IF EXISTS Piles CASCADE;
DROP SEQUENCE IF EXISTS idPile_seq;
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

DROP TABLE IF EXISTS Hands CASCADE;
DROP SEQUENCE IF EXISTS idHands_seq;
CREATE SEQUENCE idHands_seq;
CREATE TABLE Hands
(
    idHands integer NOT NULL DEFAULT nextval
    ('idPile_seq'::regclass) PRIMARY KEY,
    listCard text
);
ALTER TABLE Hands
ADD COLUMN idGame integer,
ADD FOREIGN KEY (idGame) REFERENCES Games(idGame);
ALTER TABLE Hands
ADD COLUMN idPlayers integer,
ADD FOREIGN KEY (id_users) REFERENCES Users(id_users);


DROP TABLE IF EXISTS Games;
DROP SEQUENCE IF EXISTS idGame_seq;
CREATE SEQUENCE idGame_seq;
CREATE TABLE Games
(
    idGame integer NOT NULL DEFAULT nextval
    ('idGame_seq'::regclass) PRIMARY KEY, 
    jeu text,
    idPiles text, 
    idHands text,
    idPlayers text,
    finished bool,
    debut bool,
    score text
);


ALTER TABLE Piles
ADD COLUMN idGame integer,
ADD FOREIGN KEY (idGame) REFERENCES Games(idGame);

DROP TABLE IF EXISTS Belote CASCADE;
DROP SEQUENCE IF EXISTS idBelote_seq;
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
);
ALTER TABLE Belote
ADD COLUMN idGame integer,
ADD FOREIGN KEY (idGame) REFERENCES Games(idGame);
