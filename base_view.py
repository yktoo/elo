import abc

class BaseView(object):
  """Base abstract class for all views"""

  __metaclass__ = abc.ABCMeta

  @classmethod
  @abc.abstractmethod
  def render(cls, participants, matches, options):
    """Should render the content passed in the constructor."""
    pass

