from list_loader import ListLoader
from match import Match
from errors import *

class MatchLoader(ListLoader):
  """Match loader class"""

  def __init__(self, participants):
    """Constructor. participants is a dictionary of participants to validate against"""
    super(MatchLoader, self).__init__()
    self.participants = participants

  def new_item_class(self):
    return Match

  def new_result_set(self):
    # Matches are stored in a simple list
    return []

  def add_item(self, item, result_set):
    # Make sure both participants exist
    if item.id_winner not in self.participants:
      raise DataError('Winner participant ID ({}) not found'.format(item.id_winner))
    if item.id_loser not in self.participants:
      raise DataError('Loser participant ID ({}) not found'.format(item.id_loser))
    result_set.append(item)
