-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament

CREATE TABLE players (id serial primary key, name text);
-- CREATE TABLE tournaments (tournament_id serial primary key, name text, winner integer references players(player_id));
CREATE TABLE matches (
	id serial primary key, 
	player_one integer references players(id), 
	player_two integer references players(id),
	winner integer references players(id)
);

CREATE VIEW standings as SELECT players.id, players.name,
    (SELECT count(winner) as wins FROM matches WHERE winner = players.id) as wins,
    (SELECT count(*) as matches FROM matches WHERE player_one = players.id or player_two = players.id) as matches
    FROM players;

CREATE VIEW standings_rows as SELECT id, name, wins, row_number() over(order by wins desc) from standings;

CREATE VIEW even_rows as SELECT id, name, row_number() over(order by row_number) as row from standings_rows where row_number % 2 = 0;
CREATE VIEW odd_rows as SELECT id, name, row_number() over(order by row_number) as row from standings_rows where row_number % 2 = 1;