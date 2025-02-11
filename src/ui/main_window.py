from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QLabel, QFileDialog, QComboBox, QToolBar, QStatusBar,
    QPushButton, QProgressBar, QListWidget, QGroupBox,
    QFormLayout, QSpinBox, QCheckBox, QMessageBox,
    QMenu, QAction
)
from PyQt5.QtCore import Qt, QTextCodec, QFileInfo
from PyQt5.QtGui import QIcon, QDragEnterEvent, QDropEvent
from pathlib import Path
from .dialogs import SettingsDialog, AboutDialog
from .widgets import DragDropListWidget
from utils.settings import Settings

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.settings = Settings()
        self.init_ui()
        self.setup_connections()
        self.load_settings()
        
    def init_ui(self):
        """Initialize the user interface."""
        self.setWindowTitle("Format Converter Pro")
        self.setGeometry(100, 100, 1000, 600)
        
        # Set up central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)
        
        # Create main sections
        self.create_file_list_section()
        self.create_conversion_section()
        self.create_status_section()
        
        # Create menus and toolbar
        self.create_menus()
        self.create_toolbar()
        
        # Apply style
        self.apply_style()
        
    def create_file_list_section(self):
        """Create the file list section."""
        files_group = QGroupBox("Selected Files")
        files_layout = QVBoxLayout()
        
        self.files_list = DragDropListWidget()
        self.files_list.setAcceptDrops(True)
        self.files_list.setMinimumHeight(200)
        
        files_layout.addWidget(self.files_list)
        
        # Add buttons
        buttons_layout = QHBoxLayout()
        
        self.add_files_btn = QPushButton("Add Files")
        self.add_folder_btn = QPushButton("Add Folder")
        self.clear_btn = QPushButton("Clear All")
        
        buttons_layout.addWidget(self.add_files_btn)
        buttons_layout.addWidget(self.add_folder_btn)
        buttons_layout.addWidget(self.clear_btn)
        
        files_layout.addLayout(buttons_layout)
        files_group.setLayout(files_layout)
        
        self.main_layout.addWidget(files_group)
        
    def create_conversion_section(self):
        """Create the conversion settings section."""
        conversion_group = QGroupBox("Conversion Settings")
        conversion_layout = QFormLayout()
        
        # Format selection
        self.format_combo = QComboBox()
        self.format_combo.addItems(['PDF', 'DOCX', 'TXT'])
        conversion_layout.addRow("Target Format:", self.format_combo)
        
        # Options
        self.preserve_format_cb = QCheckBox("Preserve Formatting")
        self.preserve_format_cb.setChecked(True)
        conversion_layout.addRow("Options:", self.preserve_format_cb)
        
        # Convert button
        self.convert_btn = QPushButton("Convert")
        self.convert_btn.setMinimumHeight(40)
        conversion_layout.addRow(self.convert_btn)
        
        conversion_group.setLayout(conversion_layout)
        self.main_layout.addWidget(conversion_group)
        
    def create_status_section(self):
        """Create the status section."""
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        self.main_layout.addWidget(self.progress_bar)
        
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Ready")
        
    def create_menus(self):
        """Create the application menus."""
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu('File')
        
        open_action = QAction('Open Files...', self)
        open_action.setShortcut('Ctrl+O')
        file_menu.addAction(open_action)
        
        add_folder_action = QAction('Add Folder...', self)
        file_menu.addAction(add_folder_action)
        
        file_menu.addSeparator()
        
        settings_action = QAction('Settings...', self)
        settings_action.setShortcut('Ctrl+,')
        file_menu.addAction(settings_action)
        
        file_menu.addSeparator()
        
        exit_action = QAction('Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        file_menu.addAction(exit_action)
        
        # Theme menu
        theme_menu = menubar.addMenu('Theme')
        
        light_theme_action = QAction('Light', self)
        theme_menu.addAction(light_theme_action)
        
        dark_theme_action = QAction('Dark', self)
        theme_menu.addAction(dark_theme_action)
        
        # Help menu
        help_menu = menubar.addMenu('Help')
        
        about_action = QAction('About', self)
        help_menu.addAction(about_action)
        
        docs_action = QAction('Documentation', self)
        help_menu.addAction(docs_action)
    
    def setup_connections(self):
        """Set up signal/slot connections."""
        # Button connections
        self.add_files_btn.clicked.connect(self.add_files)
        self.add_folder_btn.clicked.connect(self.add_folder)
        self.clear_btn.clicked.connect(self.clear_files)
        self.convert_btn.clicked.connect(self.start_conversion)
        
        # Menu connections
        self.findChild(QAction, 'Exit').triggered.connect(self.close)
        self.findChild(QAction, 'Settings...').triggered.connect(self.show_settings)
        self.findChild(QAction, 'About').triggered.connect(self.show_about)
    
    def apply_style(self):
        """Apply the current theme."""
        with open('src/ui/styles/default.qss', 'r') as f:
            self.setStyleSheet(f.read())
