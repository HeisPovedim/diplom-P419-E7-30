from PyQt6.QtWidgets import QMainWindow
from pyqtgraph import PlotWidget

class GraphWidget(QMainWindow):
    def __init__(self, x_data, y_data):
        super().__init__()
        
        # Настройка окна
        self.setWindowTitle("График")
        self.resize(1000, 600)

        # Создаем объект графика
        self.plot_widget = PlotWidget(self)
        self.plot_widget.plot(x_data, y_data)

        # Показываем окно с графиком
        self.setCentralWidget(self.plot_widget)