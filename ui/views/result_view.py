from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PySide6.QtGui import QPixmap
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ui.main_window import MainWindow


class ResultView(QWidget):
    def __init__(self, main_window: 'MainWindow') -> None:
        super().__init__()
        self.main_window = main_window

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.latex_label = QLabel()
        self.graph_label = QLabel()
        self.back_btn = QPushButton("Вернуться в начало")

        self.layout.addWidget(self.latex_label)
        self.layout.addWidget(self.graph_label)
        self.layout.addWidget(self.back_btn)

        self.back_btn.clicked.connect(self.main_window.show_start)

    def set_result(self, latex_path: str, graph_path: str) -> None:
        self.latex_label.setPixmap(QPixmap(latex_path))
        self.graph_label.setPixmap(QPixmap(graph_path))
