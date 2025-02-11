from pathlib import Path
from typing import Optional, Tuple
import docx
from PyPDF2 import PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from .base import BaseConverter

class TXTConverter(BaseConverter):
    """Handles TXT file conversions."""
    
    def __init__(self):
        super().__init__()
        self.supported_formats = ['pdf', 'docx']
        self.supported_encodings = ['utf-8', 'utf-16', 'windows-1255', 'iso-8859-8', 'cp1255']
    
    def convert(self, input_path: Path, output_path: Path, **kwargs) -> bool:
        """
        Convert TXT to other formats.
        
        Args:
            input_path (Path): Path to input TXT file
            output_path (Path): Path to output file
            **kwargs: Additional conversion options
                - encoding (str): Input file encoding
                - preserve_formatting (bool): Try to preserve document formatting
                
        Returns:
            bool: True if conversion successful, False otherwise
        """
        if not self.validate_input(input_path):
            return False
            
        try:
            content, encoding = self._read_file(input_path, kwargs.get('encoding'))
            
            if output_path.suffix.lower() == '.pdf':
                return self._to_pdf(content, output_path)
            elif output_path.suffix.lower() == '.docx':
                return self._to_docx(content, output_path)
            else:
                self.logger.error(f"Unsupported output format: {output_path.suffix}")
                return False
                
        except Exception as e:
            self.logger.error(f"TXT conversion failed: {str(e)}")
            return False
    
    def _read_file(self, input_path: Path, preferred_encoding: Optional[str] = None) -> Tuple[str, str]:
        """
        Read text file with encoding detection.
        
        Returns:
            Tuple[str, str]: (file content, detected encoding)
        """
        if preferred_encoding:
            try:
                with open(input_path, 'r', encoding=preferred_encoding) as f:
                    return f.read(), preferred_encoding
            except UnicodeDecodeError:
                pass
        
        # Try different encodings
        for encoding in self.supported_encodings:
            try:
                with open(input_path, 'r', encoding=encoding) as f:
                    return f.read(), encoding
            except UnicodeDecodeError:
                continue
        
        raise ValueError(f"Could not read file with any supported encoding")
    
    def _to_pdf(self, content: str, output_path: Path) -> bool:
        """Convert text content to PDF format."""
        try:
            c = canvas.Canvas(str(output_path), pagesize=letter)
            width, height = letter
            y = height - 72  # Start 1 inch from top
            
            # Split content into lines
            lines = content.split('\n')
            
            for line in lines:
                if line.strip():  # Skip empty lines
                    # Wrap long lines
                    while len(line) > 80:  # Basic line wrapping
                        wrapped_line = line[:80]
                        c.drawString(72, y, wrapped_line)
                        line = line[80:]
                        y -= 14
                        
                        if y < 72:  # New page if needed
                            c.showPage()
                            y = height - 72
                    
                    # Draw remaining text
                    if line:
                        c.drawString(72, y, line)
                
                y -= 14
                if y < 72:  # New page if needed
                    c.showPage()
                    y = height - 72
            
            c.save()
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to convert TXT to PDF: {str(e)}")
            return False
    
    def _to_docx(self, content: str, output_path: Path) -> bool:
        """Convert text content to DOCX format."""
        try:
            doc = docx.Document()
            
            # Split content into paragraphs (double newlines)
            paragraphs = content.split('\n\n')
            
            for para in paragraphs:
                if para.strip():  # Skip empty paragraphs
                    doc.add_paragraph(para.strip())
            
            doc.save(str(output_path))
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to convert TXT to DOCX: {str(e)}")
            return False
