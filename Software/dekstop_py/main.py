from PyQt6.QtWidgets import QApplication
from validators.global_validator import *

from interface.file_upload import FileUpload

if __name__ == "__main__":
    app = QApplication([])
    window = FileUpload()
    window.show()

    sys.exit(app.exec())
    