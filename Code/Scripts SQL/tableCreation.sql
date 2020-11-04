DROP TABLE IF EXISTS users
CASCADE;
DROP SEQUENCE IF EXISTS id_users;
CREATE SEQUENCE id_users_seq;
CREATE TABLE users
(
    id_users integer NOT NULL DEFAULT nextval
	('id_users_seq'
    ::regclass) PRIMARY KEY,
	username text,
    mdp text,
    admini boolean
    connected boolean);

    INSERT INTO users
        (id_users, username,mdp,admini,connecte)
    VALUES
        (1, 'admin', 'admin', TRUE, FALSE);

    """"pas complet"""
DROP TABLE IF EXISTS Pile CASCADE;
DROP SEQUENCE IF EXISTS idPile;
CREATE SEQUENCE idPile_seq;
CREATE TABLE Piles(
    idPile integer NOT NULL DEFAULT nextval
    ('idPile_seq' ::regclass) PRIMARY KEY,
    idGame integer,
    card_list 
) 