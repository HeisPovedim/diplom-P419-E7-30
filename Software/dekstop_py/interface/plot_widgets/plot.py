from pyqtgraph import PlotWidget

class PlotGraph(PlotWidget):
    def __init__(self, freq, parametr, type):
        super().__init__()
        
        # Создаем график
        self.plot(title=f"Измерение керамической пластины {type}")
        
        # Устанавливаем оси
        self.setLabel('left', type)
        self.setLabel('bottom', 'Частота')
        
        self.plot(freq, parametr)