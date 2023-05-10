import sys
import traceback as tb
from PyQt6.QtWidgets import QErrorMessage

err_dialog = None
def hook(typeexp,value,tracback):
    """Кастоманая функция валидации ошибок"""
    
    global err_dialog
    tb.print_exception(typeexp,value,tracback)
    
    err_dialog = QErrorMessage()
    err_dialog.showMessage(f'err: {str(value)}')

sys.excepthook = hook