#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#
from db import *


def deleteMatches():
    """Remove all the match records from the database."""
    DB().execute("DELETE FROM matches", True)

def deletePlayers():
    """Remove all the player records from the database."""
    DB().execute("DELETE FROM players", True)

def countPlayers():
    """Returns the number of players currently registered."""
    db = DB().execute("SELECT count(*) as sum FROM players")
    fetched = db["cursor"].fetchone()
    db["conn"].close()

    return fetched[0]

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    DB().execute("INSERT INTO players (name) VALUES (%s)", True, (name,))

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db = DB().execute("SELECT * FROM standings")
    fetched = db["cursor"].fetchall()
    db["conn"].close()
 
    return fetched

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DB().execute("INSERT INTO matches(player_one, player_two, winner) VALUES (%s,%s,%s)", True, (winner,loser,winner,))
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    db = DB().execute("select odd.id,odd.name,even.id,even.name from odd_rows as odd join even_rows as even on odd.row = even.row;")
    fetched = db["cursor"].fetchall()
    db["conn"].close()

    return fetched

def getWinner():
    """
    Returns a String, the name of the winner of the tournament.
    """
    db = DB().execute("select name from standings where wins = (select max(wins) from standings);")
    fetched = db["cursor"].fetchone()
    db["conn"].close()

    return fetched