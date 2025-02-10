import sys
from PyQt5.QtWidgets import QApplication
from file_converter_app import FileConverterApp

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FileConverterApp()
    window.show()
    sys.exit(app.exec_())