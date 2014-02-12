import abc

class Unserializable(object):
  """Base abstract class which can be unserialized from string."""

  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def set_properties(self, s):
    """Should initialize instance's properties from the string s."""
    pass
