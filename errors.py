################################################################################
# Error class declarations
################################################################################

class EloError(Exception):
  """Base class for all Elo-related exceptions."""
  pass



class FileError(EloError):
  """Exception raised for file-related errors.

  Attributes:
    fileName - path to the file
    message  - error message
  """

  def __init__(self, expr, msg):
    self.fileName = fileName
    self.message = message



class DataError(EloError):
  """Exception raised for data and parse errors."""
  pass
