import logging
import sys
from pathlib import Path
from datetime import datetime
from typing import Optional

def setup_logger(log_dir: Optional[Path] = None) -> logging.Logger:
    """
    Setup application logger with both file and console handlers.
    
    Args:
        log_dir: Directory to store log files. If None, logs only to console.
        
    Returns:
        logging.Logger: Configured logger instance
    """
    logger = logging.getLogger('format_converter')
    logger.setLevel(logging.DEBUG)
    
    # Create formatters
    detailed_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    simple_formatter = logging.Formatter(
        '%(levelname)s: %(message)s'
    )
    
    # Console handler (for user feedback)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(simple_formatter)
    logger.addHandler(console_handler)
    
    # File handler (for debugging)
    if log_dir:
        log_dir = Path(log_dir)
        log_dir.mkdir(parents=True, exist_ok=True)
        
        log_file = log_dir / f"format_converter_{datetime.now():%Y%m%d}.log"
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(detailed_formatter)
        logger.addHandler(file_handler)
    
    return logger

def get_logger(name: str) -> logging.Logger:
    """
    Get a logger instance with the specified name.
    
    Args:
        name: Name of the logger (usually __name__)
        
    Returns:
        logging.Logger: Logger instance
    """
    return logging.getLogger(f'format_converter.{name}')
