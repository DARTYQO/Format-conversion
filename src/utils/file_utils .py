from pathlib import Path
from typing import List, Optional
import shutil
import tempfile
from .exceptions import OutputError
from .logger import get_logger

logger = get_logger(__name__)

def ensure_output_dir(path: Path) -> Path:
    """
    Ensure output directory exists and is writable.
    
    Args:
        path: Directory path
        
    Returns:
        Path: Validated directory path
        
    Raises:
        OutputError: If directory cannot be created or is not writable
    """
    try:
        path.mkdir(parents=True, exist_ok=True)
        
        # Test if directory is writable
        test_file = path / '.write_test'
        try:
            test_file.touch()
            test_file.unlink()
        except Exception as e:
            raise OutputError(f"Directory is not writable: {e}")
            
        return path
    except Exception as e:
        raise OutputError(f"Failed to create output directory: {e}")

def create_temp_dir() -> Path:
    """
    Create a temporary directory for conversion process.
    
    Returns:
        Path: Path to temporary directory
    """
    return Path(tempfile.mkdtemp(prefix='format_converter_'))

def cleanup_temp_dir(temp_dir: Path) -> None:
    """
    Clean up temporary directory.
    
    Args:
        temp_dir: Path to temporary directory
    """
    try:
        shutil.rmtree(temp_dir)
    except Exception as e:
        logger.warning(f"Failed to clean up temporary directory: {e}")

def get_unique_filename(output_path: Path) -> Path:
    """
    Generate a unique filename if file already exists.
    
    Args:
        output_path: Desired output path
        
    Returns:
        Path: Unique file path
    """
    if not output_path.exists():
        return output_path
        
    counter = 1
    while True:
        new_path = output_path.with_stem(f"{output_path.stem}_{counter}")
        if not new_path.exists():
            return new_path
        counter += 1
