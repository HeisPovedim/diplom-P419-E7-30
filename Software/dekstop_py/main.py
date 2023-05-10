# PyQt6 && LIBS
from PyQt6.QtWidgets import QApplication
from validators.global_validator import *

# WINDOWS
from interface.authorization import Authorization

if __name__ == "__main__":
    app = QApplication([])
    window = Authorization()
    window.show()
    sys.exit(app.exec())
    