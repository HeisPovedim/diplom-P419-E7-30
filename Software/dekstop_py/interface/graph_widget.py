from PyQt6.QtWidgets import QMainWindow
import pyqtgraph as pg
from pyqtgraph import PlotWidget

from interface.plot_widgets.plot_fp import PlotFp

class GraphWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Настройка окна
        self.setWindowTitle("График")
        self.resize(1000, 600)

        # Инициализация интерфейса
        self.setupUi()
        
    def setupUi(self):
        """Интерфейс окна"""
        
        # Показываем окно с графиком
        self.setCentralWidget(PlotFp())