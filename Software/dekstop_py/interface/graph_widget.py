from PyQt6.QtWidgets import QMainWindow
import pyqtgraph as pg
from pyqtgraph import PlotWidget

from interface.plot_widgets.plot_fp import PlotFp
from interface.plot_widgets.plot_gp import PlotGp
from interface.plot_widgets.plot_fa import PlotFa
from interface.plot_widgets.plot_rs import PlotRs

class GraphWidget(object):
    def __init__(self):
        super().__init__()
        
        # Инициализация переменных
        self.graph_fp = None
        self.graph_gp = None
        self.graph_fa = None
        self.graph_rs = None

        # Инициализация интерфейса
        self.setupUi()
        
    def setupUi(self):
        """Интерфейс окна"""
        
        # График Fp
        self.graph_fp = QMainWindow()
        self.graph_fp.setWindowTitle("График Fp")
        self.graph_fp.resize(1000, 600)
        self.graph_fp.setCentralWidget(PlotFp())
        self.graph_fp.show()

        # График Gp
        self.graph_gp = QMainWindow()
        self.graph_gp.setWindowTitle("График Gp")
        self.graph_gp.resize(1000, 600)
        self.graph_gp.setCentralWidget(PlotGp())
        self.graph_gp.show()

        # График Gp
        self.graph_fa = QMainWindow()
        self.graph_fa.setWindowTitle("График fa")
        self.graph_fa.resize(1000, 600)
        self.graph_fa.setCentralWidget(PlotFa())
        self.graph_fa.show()

        # График Rs
        self.graph_rs = QMainWindow()
        self.graph_rs.setWindowTitle("График Rs")
        self.graph_rs.resize(1000, 600)
        self.graph_rs.setCentralWidget(PlotRs())
        self.graph_rs.show()