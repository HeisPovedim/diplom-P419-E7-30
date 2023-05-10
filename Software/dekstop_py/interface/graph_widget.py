# Plot Widget
from interface.plot_widgets.plot_fp import PlotFp
from interface.plot_widgets.plot_gp import PlotGp
from interface.plot_widgets.plot_fa import PlotFa
from interface.plot_widgets.plot_rs import PlotRs

# HELPERS
from helpers.helpers import quick_creation_QMainWindow

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
        self.graph_fp = quick_creation_QMainWindow("График Fp", 1000, 600, PlotFp())
        self.graph_fp.show()

        # График Gp
        self.graph_gp = quick_creation_QMainWindow("График Gp", 1000, 600, PlotGp())
        self.graph_gp.show()

        # График Gp
        self.graph_fa = quick_creation_QMainWindow("График fa", 1000, 600, PlotFa())
        self.graph_fa.show()

        # График Rs
        self.graph_rs = quick_creation_QMainWindow("График Rs", 1000, 600, PlotRs())
        self.graph_rs.show()