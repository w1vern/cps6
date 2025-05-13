from PySide6.QtWidgets import QWidget, QVBoxLayout
from typing import TYPE_CHECKING
from ui.views.selector_view import SelectorView
from ui.views.euler_input_view import EulerInputView
from ui.views.chebyshev_input_view import ChebyshevInputView
from ui.views.result_view import ResultView

if TYPE_CHECKING:
    from main_window import MainWindow


class CombinedView(QWidget):
    def __init__(self, main_window: 'MainWindow') -> None:
        super().__init__()
        self.main_window = main_window

        self.my_layout = QVBoxLayout()
        self.setLayout(self.my_layout)

        self.selector = SelectorView(self)
        self.euler_input = EulerInputView(self)
        self.chebyshev_input = ChebyshevInputView(self)
        self.result = ResultView(self)

        self.my_layout.addWidget(self.selector, stretch=1)
        self.my_layout.addWidget(self.euler_input, stretch=1)
        self.my_layout.addWidget(self.chebyshev_input, stretch=1)
        self.my_layout.addWidget(self.result, stretch=7)

        self.update_visibility("euler")

    def update_visibility(self, equation_type: str) -> None:
        self.euler_input.setVisible(equation_type == "euler")
        self.chebyshev_input.setVisible(equation_type == "chebyshev")
        self.result.clear_result()

    def calculate(self, equation_type: str) -> None:
        if equation_type == "euler":
            inputs = self.euler_input.get_data()
        else:
            inputs = self.chebyshev_input.get_data()
        self.main_window.calculate(equation_type, inputs)

    def set_result(self) -> None:
        self.result.set_result()


