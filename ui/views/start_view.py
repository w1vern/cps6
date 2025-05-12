from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ui.main_window import MainWindow


class StartView(QWidget):
    def __init__(self, main_window: 'MainWindow') -> None:
        super().__init__()
        self.main_window = main_window

        layout = QVBoxLayout()

        label = QLabel("Выберите тип уравнения")
        euler_btn = QPushButton("Уравнение Эйлера")
        chebyshev_btn = QPushButton("Уравнение Чебышева")

        euler_btn.clicked.connect(self.main_window.show_euler_input)
        chebyshev_btn.clicked.connect(self.main_window.show_chebyshev_input)

        layout.addWidget(label)
        layout.addWidget(euler_btn)
        layout.addWidget(chebyshev_btn)
        self.setLayout(layout)
