from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout,
                           QHBoxLayout, QPushButton, QLabel, QFileDialog,
                           QComboBox, QToolBar, QStatusBar, QProgressBar,
                           QStyle, QMessageBox, QAction, QDialog, QFormLayout,
                           QFrame, QCheckBox, QGroupBox, QListWidget, QListWidgetItem, 
                           QAbstractItemView, QMenu, QFileIconProvider, QSpinBox, QLineEdit)
from PyQt5.QtCore import Qt, QSize, QFileInfo
from PyQt5.QtGui import QIcon, QFont, QPalette, QColor
import os
import json
from .styles import STYLE_SHEET
from .converter import FileConverter

class DragDropListWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.parent = parent

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
            icon_provider = QFileIconProvider()
            
            for url in event.mimeData().urls():
                file_path = url.toLocalFile()
                if file_path.endswith(('.pdf', '.docx', '.txt')):
                    exists = False
                    for i in range(self.count()):
                        if self.item(i).data(Qt.UserRole) == file_path:
                            exists = True
                            break
                    
                    if not exists:
                        icon = icon_provider.icon(QFileInfo(file_path))
                        item = QListWidgetItem(icon, os.path.basename(file_path))
                        item.setData(Qt.UserRole, file_path)
                        self.addItem(item)
                        if self.parent:
                            self.parent.selected_files.append(file_path)
                            self.parent.status.showMessage(f"{self.count()} קבצים נבחרו")
        else:
            event.ignore()

class FileConverterUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.output_folder = os.path.join(os.path.expanduser("~"), "Documents", "FileConverter")
        self.progress_bar = None
        self.format_combo = None
        self.output_dir = None
        self.last_output_dir = None
        self.selected_files = []
        
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)
        
        icon_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "resources", "icon.ico")
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        
        self.init_ui()
        self.load_settings()
        self.setStyleSheet(STYLE_SHEET)

    def init_ui(self):
        self.setWindowTitle("Format conversion")
        self.setGeometry(100, 100, 1000, 600)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)
        
        self.create_toolbar()
        self.create_menus()
        self.create_main_frame(main_layout)
        self.create_status_bar()

    def create_toolbar(self):
        # TODO: Implement toolbar creation
        pass

    def create_menus(self):
        # TODO: Implement menu creation
        pass

    def create_main_frame(self, layout):
        # TODO: Implement main frame creation
        pass

    def create_status_bar(self):
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.status.showMessage("מוכן")

    def load_settings(self):
        settings_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "settings.json")
        if os.path.exists(settings_path):
            with open(settings_path, 'r') as f:
                settings = json.load(f)
                self.last_output_dir = settings.get('last_output_dir', None)

    def save_settings(self):
        settings_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "settings.json")
        settings = {
            'last_output_dir': self.last_output_dir
        }
        with open(settings_path, 'w') as f:
            json.dump(settings, f)
