

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QLabel, QHBoxLayout, QPushButton
from typing import List


class EulerInputView(QWidget):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.coefficients: List[QLineEdit] = []

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.coeff_layout = QVBoxLayout()
        self.add_remove_buttons(layout)

        layout.addWidget(QLabel("Коэффициенты a_i:"))
        for _ in range(3):
            self.add_coefficient()

        self.func_input = QLineEdit(placeholderText="f(x) = ")
        layout.addWidget(QLabel("Функция:"))
        layout.addWidget(self.func_input)
        layout.addLayout(self.coeff_layout)

    def add_remove_buttons(self, layout: QVBoxLayout) -> None:
        btn_layout = QHBoxLayout()
        add_btn = QPushButton("+")
        remove_btn = QPushButton("-")
        btn_layout.addWidget(add_btn)
        btn_layout.addWidget(remove_btn)
        layout.addLayout(btn_layout)

        add_btn.clicked.connect(self.add_coefficient)
        remove_btn.clicked.connect(self.remove_coefficient)

    def add_coefficient(self) -> None:
        inp = QLineEdit(placeholderText="1.0")
        self.coefficients.append(inp)
        self.coeff_layout.addWidget(inp)

    def remove_coefficient(self) -> None:
        if self.coefficients:
            inp = self.coefficients.pop()
            inp.setParent(None)

    def get_data(self) -> tuple[list[float], str]:
        return (
            [float(inp.text()) for inp in self.coefficients],
            self.func_input.text()
        )
