################################################################################
# Error class declarations
################################################################################

class EloError(Exception):
  """Base class for all Elo-related exceptions."""
  pass


class FileError(EloError):
  """Exception raised for file-related errors."""


class DataError(EloError):
  """Exception raised for data and parse errors."""
  pass
