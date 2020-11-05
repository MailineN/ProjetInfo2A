DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS id_users;
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

    INSERT INTO users
        (id_users, username,mdp,admini,connected, score)
    VALUES
        (1, 'admin', 'admin', TRUE, FALSE, NULL);

DROP TABLE IF EXISTS Games;
DROP SEQUENCE IF EXISTS idGame;
CREATE SEQUENCE idGame_seq;
CREATE TABLE Games
(
    idGames integer NOT NULL DEFAULT nextval
    ('idGames_seq'::regclass) PRIMARY KEY,
    # TODO : add users id
) 

DROP TABLE IF EXISTS Piles CASCADE;
DROP SEQUENCE IF EXISTS idPile;
CREATE SEQUENCE idPile_seq;
CREATE TABLE Piles
(
    idPile integer NOT NULL DEFAULT nextval
    ('idPile_seq'::regclass) PRIMARY KEY,
    CONSTRAINT idGame integer 
        FOREIGN KEY(idGame)
        REFERENCES Games(idGame),
    card1 text,
    card2 text,
    card3 text,
    card4 text,
) 