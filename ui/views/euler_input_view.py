from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QScrollArea
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from ui.main_window import MainWindow


class EulerInputView(QWidget):
    def __init__(self, main_window: 'MainWindow') -> None:
        super().__init__()
        self.main_window = main_window
        self.coefficient_inputs: List[QLineEdit] = []

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.coeff_layout = QVBoxLayout()
        self.coeff_container = QWidget()
        self.coeff_container.setLayout(self.coeff_layout)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(self.coeff_container)
        self.layout.addWidget(QLabel("Коэффициенты a_i:"))
        self.layout.addWidget(scroll)

        btn_layout = QHBoxLayout()
        self.add_btn = QPushButton("+")
        self.remove_btn = QPushButton("-")
        btn_layout.addWidget(self.add_btn)
        btn_layout.addWidget(self.remove_btn)
        self.layout.addLayout(btn_layout)

        self.func_input = QLineEdit()
        self.layout.addWidget(QLabel("Введите функцию"))
        self.layout.addWidget(self.func_input)

        self.solve_btn = QPushButton("Рассчитать")
        self.layout.addWidget(self.solve_btn)

        self.add_btn.clicked.connect(self.add_coefficient)
        self.remove_btn.clicked.connect(self.remove_coefficient)
        self.solve_btn.clicked.connect(self.solve)

        self.reset()

    def reset(self) -> None:
        while self.coefficient_inputs:
            self.remove_coefficient()
        for _ in range(3):
            self.add_coefficient()
        self.func_input.clear()

    def add_coefficient(self) -> None:
        line_edit = QLineEdit()
        self.coefficient_inputs.append(line_edit)
        self.coeff_layout.addWidget(line_edit)

    def remove_coefficient(self) -> None:
        if self.coefficient_inputs:
            line_edit = self.coefficient_inputs.pop()
            self.coeff_layout.removeWidget(line_edit)
            line_edit.setParent(None)

    def solve(self) -> None:
        coefficients = [inp.text() for inp in self.coefficient_inputs]
        func_text = self.func_input.text()
        # TODO: вызвать решение уравнения Эйлера здесь
        self.main_window.show_result("LATEX_EULER", "GRAPH_EULER.png")
