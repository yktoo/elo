from unserializable import Unserializable
from errors import *

class Participant(Unserializable):
  """Participant class

  Attributes:
    id   - ID of the participant
    name - name of the participant
  """

  def __init__(self):
    self.id   = None
    self.name = None

  def setProperties(self, s):
    #!!! Name can contain spaces, so a regexp is needed (?)
    a = s.split(' ')
    if len(a) != 2: raise DataError('Wrong number of arguments ({})'.format(len(a)))
    #!!! Check whether ID is indeed integer
    id   = int(a[0])
    name = a[1]
    # Check the values
    if id<0: raise DataError('Participant\'s ID cannot be negative ({} given)'.format(id))
    if name=='': raise DataError('An empty name is given for the participant with ID={}'.format(id))
    # Initialise the values
    self.id   = id
    self.name = name
