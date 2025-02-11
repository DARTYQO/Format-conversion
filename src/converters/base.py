from abc import ABC, abstractmethod
from pathlib import Path
from typing import Optional, List
import logging

class BaseConverter(ABC):
    """Base class for all file converters."""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.supported_formats: List[str] = []
    
    @abstractmethod
    def convert(self, input_path: Path, output_path: Path, **kwargs) -> bool:
        """
        Convert a file from one format to another.
        
        Args:
            input_path (Path): Path to input file
            output_path (Path): Path to output file
            **kwargs: Additional conversion options
            
        Returns:
            bool: True if conversion successful, False otherwise
        """
        pass
    
    def validate_input(self, input_path: Path) -> bool:
        """
        Validate input file before conversion.
        
        Args:
            input_path (Path): Path to input file
            
        Returns:
            bool: True if file is valid, False otherwise
        """
        if not input_path.exists():
            self.logger.error(f"Input file not found: {input_path}")
            return False
        
        if not input_path.is_file():
            self.logger.error(f"Input path is not a file: {input_path}")
            return False
            
        return True
    
    def validate_output(self, output_path: Path) -> bool:
        """
        Validate output path before conversion.
        
        Args:
            output_path (Path): Path to output file
            
        Returns:
            bool: True if path is valid, False otherwise
        """
        try:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            return True
        except Exception as e:
            self.logger.error(f"Failed to create output directory: {e}")
            return False
