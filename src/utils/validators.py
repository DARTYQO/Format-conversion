from pathlib import Path
from typing import List, Optional
import magic  # python-magic library for file type detection
from .exceptions import ValidationError
from .logger import get_logger

logger = get_logger(__name__)

def validate_file(file_path: Path, 
                 allowed_formats: Optional[List[str]] = None,
                 max_size: Optional[int] = None) -> bool:
    """
    Validate a file before conversion.
    
    Args:
        file_path: Path to the file
        allowed_formats: List of allowed file extensions (without dot)
        max_size: Maximum file size in bytes
        
    Returns:
        bool: True if file is valid
        
    Raises:
        ValidationError: If validation fails
    """
    try:
        # Check if file exists
        if not file_path.exists():
            raise ValidationError(f"File not found: {file_path}")
            
        # Check if it's a file
        if not file_path.is_file():
            raise ValidationError(f"Not a file: {file_path}")
            
        # Check file format
        if allowed_formats:
            if file_path.suffix.lower().lstrip('.') not in allowed_formats:
                raise ValidationError(
                    f"Unsupported file format: {file_path.suffix}. "
                    f"Supported formats: {', '.join(allowed_formats)}"
                )
        
        # Check file size
        if max_size and file_path.stat().st_size > max_size:
            size_mb = max_size / (1024 * 1024)
            raise ValidationError(
                f"File too large. Maximum size: {size_mb:.1f}MB"
            )
        
        # Check if file is readable
        try:
            file_path.open('rb').close()
        except Exception as e:
            raise ValidationError(f"File is not readable: {e}")
        
        # Check actual file type using python-magic
        try:
            mime = magic.from_file(str(file_path), mime=True)
            if not is_valid_mime_type(mime, allowed_formats):
                raise ValidationError(
                    f"File content doesn't match its extension: {mime}"
                )
        except Exception as e:
            logger.warning(f"Could not verify file type with magic: {e}")
        
        return True
        
    except ValidationError:
        raise
    except Exception as e:
        raise ValidationError(f"Validation failed: {e}")

def is_valid_mime_type(mime: str, allowed_formats: Optional[List[str]]) -> bool:
    """
    Check if MIME type matches allowed formats.
    
    Args:
        mime: MIME type string
        allowed_formats: List of allowed extensions
        
    Returns:
        bool: True if MIME type is valid
    """
    if not allowed_formats:
        return True
        
    mime_map = {
        'pdf': 'application/pdf',
        'docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        'txt': 'text/plain'
    }
    
    return any(mime == mime_map.get(fmt) for fmt in allowed_formats)
