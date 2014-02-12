from unserializable import Unserializable
from errors import *

class Participant(Unserializable):
  """Participant class

  Attributes:
    id   - ID of the participant
    name - name of the participant
  """

  # Standard K-factor value
  k_factor = 16
  # Default average rating value
  default_rating = 1500

  def __init__(self):
    self.id         = None
    self.name       = None
    self.rating     = self.default_rating
    self.num_wins   = 0
    self.num_losses = 0
    self.rank       = None

  def set_properties(self, s):
    # Parse the fields
    a = s.split(' ', 1)
    if len(a) != 2: raise DataError('Wrong number of arguments ({})'.format(len(a)))
    # Validate ID
    try:
      self.id   = int(a[0].strip())
    except ValueError as e:
      raise DataError('Invalid participant ID: '+str(e))
    if self.id<0: raise DataError('Participant\'s ID cannot be negative ({} given)'.format(self.id))
    # Validate name
    self.name = a[1].strip()
    if self.name=='': raise DataError('An empty name is given for the participant with ID={}'.format(self.id))

  def expected_score(self, opponent_rating):
    """Returns the expected score for the participant"""
    return 1 / (1 + 10**((opponent_rating-self.rating)/400))

  def update_rating(self, opponent_rating, score):
    """Updates participant's Elo rating"""
    self.rating += self.k_factor*(score - self.expected_score(opponent_rating))

  def won(self, opponent_rating):
    """Denotes that the participant has defeated the opponent"""
    self.num_wins += 1
    self.update_rating(opponent_rating, 1)

  def lost(self, opponent_rating):
    """Denotes that the participant has lost to the opponent"""
    self.num_losses += 1
    self.update_rating(opponent_rating, 0)
