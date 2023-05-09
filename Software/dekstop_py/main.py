from PyQt6.QtWidgets import QApplication
from validators.global_validator import *

from interface.authorization import Authorization
from interface.personal_account import PersonalAccount

if __name__ == "__main__":
    app = QApplication([])
    window = PersonalAccount()
    window.show()
    sys.exit(app.exec())
    