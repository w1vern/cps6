from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtSvgWidgets import QSvgWidget

import xml.etree.ElementTree as ET


def get_svg_aspect_ratio(path: str) -> float:
    tree = ET.parse(path)
    root = tree.getroot()

    width = root.get("width")
    height = root.get("height")

    if width is None or height is None:
        viewBox = root.get("viewBox")
        if viewBox:
            _, _, w, h = map(float, viewBox.strip().split())
            return w / h
        else:
            raise ValueError("SVG must have width/height or viewBox")

    def parse_dim(value: str) -> float:
        return float(value.replace("pt", "").strip())

    return parse_dim(width) / parse_dim(height)


class ResultView(QWidget):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)

        self.my_layout = QVBoxLayout()
        self.setLayout(self.my_layout)

        self.latex_widget = QSvgWidget()
        self.graph_widget = QSvgWidget()

        self.latex_container = QWidget()
        self.graph_container = QWidget()

        self.latex_layout = QVBoxLayout(self.latex_container)
        self.graph_layout = QVBoxLayout(self.graph_container)

        self.latex_layout.addWidget(self.latex_widget)
        self.graph_layout.addWidget(self.graph_widget)

        self.my_layout.addWidget(self.latex_container, stretch=3)
        self.my_layout.addWidget(self.graph_container, stretch=7)

    def resizeEvent(self, event) -> None:
        self._rescale()
        super().resizeEvent(event)

    def _rescale(self) -> None:
        latex_ratio = get_svg_aspect_ratio("render/latex.svg")
        graph_ratio = get_svg_aspect_ratio("render/function.svg")

        latex_container_width = self.latex_container.width()
        graph_container_width = self.graph_container.width()

        latex_height = int(latex_container_width / latex_ratio)
        graph_height = int(graph_container_width / graph_ratio)

        self.latex_widget.setFixedSize(latex_container_width, latex_height)
        self.graph_widget.setFixedSize(graph_container_width, graph_height)


    def set_result(self) -> None:
        self.latex_widget.load("render/latex.svg")
        self.graph_widget.load("render/function.svg")
        self._rescale()

    def clear_result(self) -> None:
        self.latex_widget.load(b"")
        self.graph_widget.load(b"")
