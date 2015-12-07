#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

from tournament_dao import *

def runTournament():
    """
    run a simulated tournament
    """
    players = 8
    deleteMatches()
    deletePlayers()
    addPlayers(players)
    calculateMatches(players)
    name = getWinner()
    print "winner: {name}!".format(name=name[0])


def addPlayers(numPlayers):
    """
    Add players to the simulated tournament
    """
    for i in range(8):
        player = "player " + str(i)
        registerPlayer(player)


def calculateMatches(numMatches):
    """
    Calculate the matches for the simulated tournament.
    """
    standings = playerStandings()
    [id1, id2, id3, id4, id5, id6, id7, id8] = [row[0] for row in standings]
    reportMatch(id1, id2)
    reportMatch(id3, id4)
    reportMatch(id5, id6)
    reportMatch(id7, id8)
    for i in range((numMatches / 2) - 1):
        pairings = swissPairings()
        [id1, id2, id3, id4] = [row[0] for row in pairings]
        [id5, id6, id7, id8] = [row[2] for row in pairings]
        reportMatch(id1, id5)
        reportMatch(id2, id6)
        reportMatch(id3, id7)
        reportMatch(id4, id8)


if __name__ == '__main__':
    runTournament()
