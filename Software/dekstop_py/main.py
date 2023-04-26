import sys
import traceback as tb

from PyQt6.QtWidgets import QApplication
from PyQt6 import QtWidgets

from interface.file_upload import FileUpload

error_messages = None
def exception_hook(exctype, value, traceback):
    
    tb.print_exception(exctype, value, traceback)
    
    global error_messages
    error_messages = QtWidgets.QErrorMessage()
    error_messages.showMessage(f"Произошла ошибка: {str(value)}")
    
sys.excepthook = exception_hook

if __name__ == "__main__":
    app = QApplication([])
    window = FileUpload()
    window.show()
    sys.exit(app.exec())
    