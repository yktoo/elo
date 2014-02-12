from unserializable import Unserializable
from errors import *

class Match(Unserializable):
  """Match class

  Attributes:
    idWinner - ID of the participant who won the match
    idLoser  - ID of the participant who lost the match
  """

  def __init__(self):
    self.idWinner = None
    self.idLoser  = None

  def setProperties(self, s):
    a = s.split(' ')
    if len(a) != 2: raise DataError('Wrong number of arguments ({})'.format(len(a)))
    #!!! Check whether these are indeed integers
    id_1 = int(a[0])
    id_2 = int(a[1])
    # Participant ID cannot be negative
    if id_1<0: raise DataError('Match winner\'s ID cannot be negative ({} given)'.format(id_1))
    if id_2<0: raise DataError('Match loser\'s ID cannot be negative ({} given)'.format(id_2))
    # One cannot have a match against themselves
    if id_1==id_2:
      raise DataError('A match must be held with two different participants, whereas the same ID given ({})'.format(id_1))
    # Initialise the values
    self.idWinner = id_1
    self.idLoser  = id_2

