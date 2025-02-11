from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, 
    QLabel, QLineEdit, QPushButton,
    QGroupBox, QFormLayout, QCheckBox,
    QComboBox, QFileDialog
)
from PyQt5.QtCore import Qt
from pathlib import Path

class SettingsDialog(QDialog):
    """Settings dialog for the application."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
        
    def init_ui(self):
        """Initialize the user interface."""
        self.setWindowTitle("Settings")
        self.setMinimumWidth(400)
        
        layout = QVBoxLayout(self)
        
        # Output directory settings
        output_group = QGroupBox("Output Directory")
        output_layout = QHBoxLayout()
        
        self.output_dir_edit = QLineEdit()
        browse_btn = QPushButton("Browse...")
        browse_btn.clicked.connect(self.browse_output_dir)
        
        output_layout.addWidget(self.output_dir_edit)
        output_layout.addWidget(browse_btn)
        output_group.setLayout(output_layout)
        layout.addWidget(output_group)
        
        # Conversion settings
        conversion_group = QGroupBox("Conversion Settings")
        conversion_layout = QFormLayout()
        
        self.default_format_combo = QComboBox()
        self.default_format_combo.addItems(['PDF', 'DOCX', 'TXT'])
        conversion_layout.addRow("Default Format:", self.default_format_combo)
        
        self.preserve_format_cb = QCheckBox("Preserve Formatting by Default")
        conversion_layout.addRow(self.preserve_format_cb)
        
        conversion_group.setLayout(conversion_layout)
        layout.addWidget(conversion_group)
        
        # Buttons
        buttons_layout = QHBoxLayout()
        ok_btn = QPushButton("OK")
        cancel_btn = QPushButton("Cancel")
        
        ok_btn.clicked.connect(self.accept)
        cancel_btn.clicked.connect(self.reject)
        
        buttons_layout.addWidget(ok_btn)
        buttons_layout.addWidget(cancel_btn)
        layout.addLayout(buttons_layout)
        
    def browse_output_dir(self):
        """Open directory browser dialog."""
        dir_path = QFileDialog.getExistingDirectory(
            self,
            "Select Output Directory",
            self.output_dir_edit.text()
        )
        if dir_path:
            self.output_dir_edit.setText(dir_path)
