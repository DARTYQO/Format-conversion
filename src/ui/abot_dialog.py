from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QLabel,
    QPushButton, QHBoxLayout
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class AboutDialog(QDialog):
    """About dialog for the application."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
        
    def init_ui(self):
        """Initialize the user interface."""
        self.setWindowTitle("About Format Converter Pro")
        self.setFixedSize(400, 300)
        
        layout = QVBoxLayout(self)
        layout.setSpacing(20)
        
        # Logo
        logo_label = QLabel()
        logo_label.setPixmap(QPixmap("src/resources/icons/app_icon.png").scaled(
            64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation
        ))
        logo_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(logo_label)
        
        # App name and version
        name_label = QLabel("Format Converter Pro")
        name_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        name_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(name_label)
        
        version_label = QLabel("Version 2.0.0")
        version_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(version_label)
        
        # Description
        desc_label = QLabel(
            "An advanced file conversion utility for converting between "
            "various document formats with support for PDF, DOCX, and TXT files."
        )
        desc_label.setWordWrap(True)
        desc_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(desc_label)
        
        # Copyright
        copyright_label = QLabel("© 2024 DARTYQO")
        copyright_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(copyright_label)
        
        # Close button
        button_layout = QHBoxLayout()
        close_btn = QPushButton("Close")
        close_btn.clicked.connect(self.accept)
        button_layout.addWidget(close_btn)
        layout.addLayout(button_layout)
