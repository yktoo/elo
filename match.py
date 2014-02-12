from unserializable import Unserializable
from errors import *

class Match(Unserializable):
  """Match class

  Attributes:
    id_winner - ID of the participant who won the match
    id_loser  - ID of the participant who lost the match
  """

  def __init__(self):
    self.id_winner = None
    self.id_loser  = None

  def set_properties(self, s):
    # Parse the fields
    a = s.split(' ')
    if len(a) != 2: raise DataError('Wrong number of arguments ({})'.format(len(a)))
    # Validate winner ID
    try:
      self.id_winner = int(a[0].strip())
    except ValueError as e:
      raise DataError('Invalid match winner participant ID: '+str(e))
    # Validate loser ID
    try:
      self.id_loser = int(a[1].strip())
    except ValueError as e:
      raise DataError('Invalid loser participant ID: '+str(e))
    # Participant ID cannot be negative
    if self.id_winner<0: raise DataError('Match winner ID cannot be negative ({} given)'.format(self.id_winner))
    if self.id_loser<0:  raise DataError('Match loser ID cannot be negative ({} given)'.format(self.id_loser))
     # One cannot have a match against themselves
    if self.id_winner==self.id_loser:
       raise DataError('A match must be held with two different participants, whereas the same ID given ({})'.format(self.id_winner))
