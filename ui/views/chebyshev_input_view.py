


from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit


class ChebyshevInputView(QWidget):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)

        layout = QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(QLabel("Степень уравнения:"))
        self.degree_input = QLineEdit()
        layout.addWidget(self.degree_input)

    def get_data(self) -> float:
        return float(self.degree_input.text())



