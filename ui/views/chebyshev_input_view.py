from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from typing import TYPE_CHECKING
from solver import solve_Chebyshev
from plotter import plot_function, plot_latex

if TYPE_CHECKING:
    from ui.main_window import MainWindow


class ChebyshevInputView(QWidget):
    def __init__(self, main_window: 'MainWindow') -> None:
        super().__init__()
        self.main_window = main_window

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label = QLabel("Введите степень уравнения")
        self.input = QLineEdit()
        self.solve_btn = QPushButton("Рассчитать")

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.input)
        self.layout.addWidget(self.solve_btn)

        self.solve_btn.clicked.connect(self.solve)

    def reset(self) -> None:
        self.input.clear()

    def solve(self) -> None:
        degree = self.input.text()

        f = solve_Chebyshev(float(degree))
        plot_function(f)
        plot_latex(f)

        self.main_window.show_result()
