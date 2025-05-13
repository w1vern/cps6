from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QSize
from typing import TYPE_CHECKING
from plotter.config import Config

if TYPE_CHECKING:
    from ui.main_window import MainWindow


class ResultView(QWidget):
    def __init__(self, main_window: 'MainWindow') -> None:
        super().__init__()
        self.main_window = main_window

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.latex_label = QLabel()
        self.latex_label.setAlignment(Qt.AlignCenter)

        self.graph_label = QLabel()
        self.graph_label.setAlignment(Qt.AlignCenter)

        self.back_btn = QPushButton("Вернуться в начало")

        self.layout.addWidget(self.latex_label)
        self.layout.addWidget(self.graph_label)
        self.layout.addWidget(self.back_btn)

        self.back_btn.clicked.connect(self.main_window.show_start)

        self.latex_pixmap = None
        self.graph_pixmap = None

    def set_result(self) -> None:
        self.latex_pixmap = QPixmap(f"{Config.output_dir}/latex.png")
        self.graph_pixmap = QPixmap(f"{Config.output_dir}/function.png")
        self._update_images()

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        self._update_images()

    def _update_images(self) -> None:
        if self.latex_pixmap and not self.latex_pixmap.isNull():
            scaled_latex = self.latex_pixmap.scaled(
                self.latex_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
            )
            self.latex_label.setPixmap(scaled_latex)

        if self.graph_pixmap and not self.graph_pixmap.isNull():
            scaled_graph = self.graph_pixmap.scaled(
                self.graph_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
            )
            self.graph_label.setPixmap(scaled_graph)
