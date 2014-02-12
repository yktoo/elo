import abc

class Unserializable(object):
  """Base class which can be unserialized from string"""

  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def setProperties(self, s):
    """Should initialize instance's properties from the string s"""
    pass

