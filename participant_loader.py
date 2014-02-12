from list_loader import ListLoader
from participant import Participant
from errors import *

class ParticipantLoader(ListLoader):
  """Participant loader class"""

  def new_item_class(self):
    return Participant

  def new_result_set(self):
    # Participants are stored in a dictionary indexed by ID
    return {}

  def add_item(self, item, result_set):
    # Check there's no participant with this ID yet
    if item.id in result_set: raise DataError('Duplicate participant ID ({})'.format(item.id))
    result_set[item.id] = item
