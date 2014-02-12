#!/usr/bin/env python
################################################################################
# This is a declaration of the main application class Elo
################################################################################

import sys
from participant import Participant
from participant_loader import ParticipantLoader
from match import Match
from match_loader import MatchLoader

#-------------------------------------------------------------------------------
# The main application class
#-------------------------------------------------------------------------------

class Elo(object):

  # Default view file name
  default_view_file_name = 'view_players_scores'

  # Default view options
  default_view_options = ''

  def __init__(self, args):
    """Constructor. Initializes all objects, load the data."""
    # Validate arguments
    if not (len(args) in [3, 4, 5]): self.usage()
    self.fileName_Names   = args[1]
    self.fileName_Matches = args[2]
    self.fileName_View    = args[3] if len(args)>3 else self.default_view_file_name
    self.viewOpts         = args[4] if len(args)>4 else self.default_view_options

  def load_data(self):
    """Loads data from the files specified on the command line"""
    # Load names
    self.participants = ParticipantLoader().load_from_file(self.fileName_Names)
    # Load matches
    self.matches = MatchLoader(self.participants).load_from_file(self.fileName_Matches)

  def calculate_ratings(self):
    """Calculates Elo ratings for each participant"""
    for match in self.matches:
      # Fetch the corresponding participants
      winner = self.participants[match.id_winner]
      loser  = self.participants[match.id_loser]
      # Save their original ratings
      old_winner_rating = winner.rating
      old_loser_rating  = loser.rating
      # Calculate new ratings
      winner.won(old_loser_rating)
      loser.lost(old_winner_rating)

  def rank_players(self):
    """Assigns a rank to each player based on their rating"""
    rank = 1
    for p in sorted(self.participants.values(), lambda x,y: int(y.rating)-int(x.rating)):
      p.rank = rank
      rank += 1

  def render_view(self):
    """Renders the data using the specified view"""
    view_module = __import__(self.fileName_View)
    view_module.View.render(self.participants, self.matches, self.viewOpts)

  def run(self):
    """The main execution method"""
    # Load the files
    self.load_data()
    # Calculate Elo ratings
    self.calculate_ratings()
    # Rank players based on the rating
    self.rank_players()
    # Render the end result
    self.render_view()

  def usage(self):
    """Prints out program usage information and exits"""
    print "Usage: elo.py <names_file> <matches_file> [<view_file>] [<view_options>]"
    sys.exit(1)

if __name__ == '__main__':
  elo = Elo(sys.argv)
  elo.run()
