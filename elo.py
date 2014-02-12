#!/usr/bin/env python
################################################################################
# This is a declaration of the main application class Elo
################################################################################

from participant import Participant
from match import Match

#-------------------------------------------------------------------------------
# The main application class
#-------------------------------------------------------------------------------

class Elo:

  # Constructor
  def __init__(self, fileName_Names, fileName_Matches):
    self.matches = {}
    self.participants = {}
    # Load names
    self.names_loadFromFile(fileName_Names)
    # Load matches
    self.matches_loadFromFile(fileName_Matches)

  def matches_loadFromFile(self, fileName):
    i = 0
    with open(fileName, 'r') as f:
      for line in f:
        m = Match()
        m.setProperties(line)
        self.matches[i] = m
        print m.idWinner, m.idLoser

  def names_loadFromFile(self, fileName):
    pass


  def run(self):
    pass

if __name__ == '__main__':
  elo = Elo('./names.txt', './matches.txt')
  elo.run()
