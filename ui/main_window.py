from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from ui.views.start_view import StartView
from ui.views.euler_input_view import EulerInputView
from ui.views.chebyshev_input_view import ChebyshevInputView
from ui.views.result_view import ResultView
import sys

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Решатель дифференциальных уравнений")
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)
        
        self.setFixedSize(800, 600)

        self.start_view = StartView(self)
        self.euler_view = EulerInputView(self)
        self.chebyshev_view = ChebyshevInputView(self)
        self.result_view = ResultView(self)

        self.stack.addWidget(self.start_view)
        self.stack.addWidget(self.euler_view)
        self.stack.addWidget(self.chebyshev_view)
        self.stack.addWidget(self.result_view)

        self.stack.setCurrentWidget(self.start_view)

    def show_start(self) -> None:
        self.stack.setCurrentWidget(self.start_view)

    def show_euler_input(self) -> None:
        self.euler_view.reset()
        self.stack.setCurrentWidget(self.euler_view)

    def show_chebyshev_input(self) -> None:
        self.chebyshev_view.reset()
        self.stack.setCurrentWidget(self.chebyshev_view)

    def show_result(self) -> None:
        self.result_view.set_result()
        self.stack.setCurrentWidget(self.result_view)
