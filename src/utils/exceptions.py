class ConversionError(Exception):
    """Base exception for conversion errors."""
    pass

class FileNotFoundError(ConversionError):
    """Raised when input file is not found."""
    pass

class UnsupportedFormatError(ConversionError):
    """Raised when file format is not supported."""
    pass

class EncodingError(ConversionError):
    """Raised when file encoding is not supported."""
    pass

class ValidationError(ConversionError):
    """Raised when file validation fails."""
    pass

class PermissionError(ConversionError):
    """Raised when there are insufficient permissions."""
    pass

class OutputError(ConversionError):
    """Raised when there's an error with the output file/directory."""
    pass

class ConversionTimeout(ConversionError):
    """Raised when conversion takes too long."""
    pass
