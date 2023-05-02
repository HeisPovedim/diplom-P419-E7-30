from PyQt6.QtWidgets import QApplication

from interface.file_upload import FileUpload
from database.connect import Connection
from validators.global_validator import *

if __name__ == "__main__":
    app = QApplication([])
    window = FileUpload()
    window.show()
    Connection()
    sys.exit(app.exec())
    