from solver import solve_Euler
from solver import solve_Chebyshev
from ui.main_window import MainWindow

class Controller:
    def __init__(self, window: MainWindow):
        self.window = window
        self._connect_signals()

    def _connect_signals(self):
        self.window.solve_button.clicked.connect(self.solve)

    def solve(self):
        equation_type = self.window.combo.currentText()
        if equation_type == "Уравнение Эйлера":
            solve_Euler([], "")
        elif equation_type == "Уравнение Чебышева":
            solve_Chebyshev(0)
