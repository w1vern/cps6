from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ui.views.combined_view import CombinedView


class SelectorView(QWidget):
    def __init__(self, parent: 'CombinedView') -> None:
        super().__init__()
        self.my_parent = parent

        layout = QHBoxLayout()
        self.setLayout(layout)

        label = QLabel("Выберите тип уравнения:")
        euler_btn = QPushButton("Эйлера")
        chebyshev_btn = QPushButton("Чебышева")
        calc_btn = QPushButton("Рассчитать")

        euler_btn.clicked.connect(lambda: self.my_parent.update_visibility("euler"))
        chebyshev_btn.clicked.connect(lambda: self.my_parent.update_visibility("chebyshev"))
        calc_btn.clicked.connect(lambda: self.my_parent.calculate(self.current_equation_type()))

        layout.addWidget(label)
        layout.addWidget(euler_btn)
        layout.addWidget(chebyshev_btn)
        layout.addWidget(calc_btn)

        self._current_type = "euler"

        euler_btn.clicked.connect(lambda: self._set_type("euler"))
        chebyshev_btn.clicked.connect(lambda: self._set_type("chebyshev"))

    def _set_type(self, eq_type: str) -> None:
        self._current_type = eq_type

    def current_equation_type(self) -> str:
        return self._current_type
