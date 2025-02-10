from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QFileIconProvider
from PyQt5.QtCore import Qt, QFileInfo
import os

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
                    # בדיקה אם הקובץ כבר קיים ברשימה
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
