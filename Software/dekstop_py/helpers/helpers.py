# PyQt6 && LIBS
from PyQt6 import QtWidgets
from hashlib import sha256

def hash_generation(value):
    """Функция хеширования"""
    
    result = sha256(str(value).encode('utf-8')).hexdigest()
    return result

def quick_creation_QMainWindow(title, width, height, elem):
    """Быстрое создание новых окон с пред-настройками"""
    
    window = QtWidgets.QMainWindow()
    window.setWindowTitle(title)
    window.resize(width, height)
    window.setCentralWidget(elem)
    
    return window
    
    