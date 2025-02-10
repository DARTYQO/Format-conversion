STYLE_SHEET = """
QMainWindow {
    background-color: #f5f5f5;
}

QToolBar {
    background-color: transparent;
    border: none;
    padding: 0;
    spacing: 0;
}

QToolButton {
    background-color: transparent;
    border: none;
    padding: 0;
}

QStatusBar {
    background-color: #e0e0e0;
    color: #333333;
}

QPushButton {
    background-color: #ffffff;
    color: #333333;
    border: 1px solid #cccccc;
    border-radius: 4px;
    padding: 8px 16px;
    min-width: 100px;
}

QPushButton:hover {
    background-color: #f0f0f0;
    border-color: #999999;
}

QPushButton:pressed {
    background-color: #e0e0e0;
}

QPushButton#formatButton {
    min-width: 80px;
    min-height: 80px;
    padding: 10px;
    margin: 5px;
    border-radius: 8px;
    font-weight: bold;
}

QPushButton#formatButton:checked {
    background-color: #e3f2fd;
    border: 2px solid #2196f3;
}

QComboBox {
    background-color: #ffffff;
    color: #333333;
    border: 1px solid #cccccc;
    border-radius: 4px;
    padding: 5px;
    min-width: 150px;
}

QListWidget {
    background-color: #f5f5f5;
    border: 1px solid #cccccc;
    border-radius: 4px;
    color: #333333;
}

QListWidget::item {
    border-bottom: 1px solid #cccccc;
}

QListWidget::item:selected {
    background-color: #e0e0e0;
}

QProgressBar {
    border-radius: 4px;
    background-color: #e0e0e0;
    text-align: center;
    color: #333333;
}

QProgressBar::chunk {
    background-color: #cccccc;
    border-radius: 4px;
}

QFrame#mainFrame {
    background-color: #f5f5f5;
    border: 1px solid #cccccc;
    border-radius: 8px;
}

QGroupBox {
    border: 1px solid #cccccc;
    border-radius: 6px;
    margin-top: 1em;
    padding-top: 10px;
}

QGroupBox::title {
    subcontrol-origin: margin;
    left: 10px;
    padding: 0 3px;
}
"""
