import sys
import traceback as tb
from PyQt6.QtWidgets import QErrorMessage

error_dialog = None
def hook(type, value, traceback):
    global error_dialog
    tb.print_exception(type, value, traceback)
    error_dialog = QErrorMessage()
    error_dialog.showMessage(f"{str(value)}")
    
sys.excepthook = hook