import abc
from unserializable import Unserializable
from errors import *

class ListLoader(object):
  """Base abstract class for loading lists from text files"""

  __metaclass__ = abc.ABCMeta

  def __init__(self):
    """Constructor"""
    # Cache and validate new item class
    self.item_class = self.new_item_class()
    if not issubclass(self.item_class, Unserializable):
      raise EloError('Class "{}" is not a descendant of Unserializable'.format(self.item_class))

  def load_from_file(self, file_name):
    """Loads a list of objects from the specified file"""
    # Initialise the result set
    result_set = self.new_result_set()
    # Open the file
    line_num = 0
    with open(file_name, 'r') as f:
      # Read in the file line by line
      for line in f:
        line_num += 1
        # Create a new instance of the final class
        item = self.item_class()
        try:
          # Load the instance's properties
          item.set_properties(line)
          # Add the instance to the result set
          self.add_item(item, result_set)
        except EloError as e:
          raise FileError('Error in file "{}" (line {}): {}'.format(file_name, line_num, str(e)))
    return result_set

  @abc.abstractmethod
  def new_item_class(self):
    """Should return the class for new items, a descendant of Unserializable."""
    pass

  @abc.abstractmethod
  def new_result_set(self):
    """Should return a new instance of the result set."""
    pass

  @abc.abstractmethod
  def add_item(self, item, result_set):
    """Should add the specified item to the result set."""
    pass
