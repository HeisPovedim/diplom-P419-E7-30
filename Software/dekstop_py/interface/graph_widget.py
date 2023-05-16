# PyQt6 && LIBS
from PyQt6 import QtWidgets

# Plot Widget
from interface.plot_widgets.plot import PlotGraph

# DATABASE
from database.requests import get_parameters

# HELPERS
from helpers.helpers import quick_creation_QMainWindow

class GraphWidget(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Настройка окна
        self.setWindowTitle("Меню графиков")
        self.setFixedSize(298, 84)
        self.setCentralWidget(QtWidgets.QWidget())
        
        # Инициализация переменных
        self.graph_phi = None
        self.graph_gp = None
        self.graph_rp = None
        self.graph_cp = None

        # Инициализация интерфейса
        self.setupUi()
        
    def setupUi(self):
        """Интерфейс окна"""
        
        # Создание меню
        grid = QtWidgets.QGridLayout()
        
        grid.addWidget(QtWidgets.QLabel("ID Объекта:"), 0, 0)
        input_object = QtWidgets.QLineEdit()
        select_graph = QtWidgets.QComboBox()
        select_graph.addItems([
            "График АЧХ",
            "График ФЧХ",
            "График зависимости проводимости Gp от частоты F",
            "График зависимости емкости Cp от частоты F",
            "График зависимости сопротивления Rp от частоты F",
            "График зависимости угла Phi от частоты F"
        ])
        btn_start = QtWidgets.QPushButton("Построить графики")
        btn_start.clicked.connect(lambda: self.build_graphs(
            input_object.text(),
            select_graph.currentText()
        ))
        
        grid.addWidget(input_object, 0, 1)
        grid.addWidget(select_graph, 1, 0, 1, 2)
        grid.addWidget(btn_start, 2, 0, 1, 2)
        
        self.centralWidget().setLayout(grid)
        
    def build_graphs(self, id, current_select):
        """Функция построения графиков"""
        
        id_parameters = []
        freq = []
        z_real_path_parameters = []
        z_imaginary_part_parameters = []
        phi_parameters = []
        gp_parameters = []
        rp_parameters = []
        cp_parameters = []
        
        for result in get_parameters(id, False):  # получение всех параметров
            
            id_parameters.append(result[0])
            freq.append(result[1])
            z_real_path_parameters.append(result[2])
            z_imaginary_part_parameters.append(result[3])
            phi_parameters.append(result[4])
            gp_parameters.append(result[5])
            rp_parameters.append(result[6])
            cp_parameters.append(result[7])
        
        if current_select == "График АЧХ":
            pass
        elif current_select == "График ФЧХ":
            pass
        elif current_select == "График зависимости проводимости Gp от частоты F":
            self.graph_gp = quick_creation_QMainWindow(
                "График Gp", 1000, 600,
                PlotGraph(freq, gp_parameters, "Gp")
            )
            self.graph_gp.show()
        elif current_select == "График зависимости емкости Cp от частоты F":
            self.graph_cp = quick_creation_QMainWindow(
                "График Cp", 1000, 600,
                PlotGraph(freq, cp_parameters, "Cp"))
            self.graph_cp.show()
        elif current_select == "График зависимости сопротивления Rp от частоты F":
            self.graph_rp = quick_creation_QMainWindow(
                "График Rp", 1000, 600,
                PlotGraph(freq, rp_parameters, "Rp"))
            self.graph_rp.show()
        elif current_select == "График зависимости угла Phi от частоты F":
            self.graph_phi = quick_creation_QMainWindow(
                "График Phi", 1000, 600,
                PlotGraph(freq, phi_parameters, "Phi")
            )
            self.graph_phi.show()