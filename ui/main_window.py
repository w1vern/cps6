
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from solver.Euler import solve_Euler
from ui.views.combined_view import CombinedView
from PySide6.QtGui import QPalette, QGuiApplication

from solver import solve_Chebyshev
from plotter import plot_function, plot_latex


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Решатель дифференциальных уравнений")

        screen = QGuiApplication.primaryScreen()
        screen_size = screen.availableGeometry()
        screen_width = screen_size.width()
        screen_height = screen_size.height()

        window_width = int(screen_width * 0.3)
        window_height = int(screen_height * 0.9)

        self.setFixedSize(window_width, window_height)
        #self.setFixedSize(800, 1000)
        # self.setWindowFlags(self.windowFlags() & ~Qt.WindowType.WindowMaximizeButtonHint)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.combined_view = CombinedView(self)
        layout.addWidget(self.combined_view)

    def calculate(self, equation_type: str, inputs: tuple[list[float], str] | float) -> None:
        palette = QApplication.palette()
        is_dark = palette.color(QPalette.ColorRole.Window).value() < 128
        try:
            if isinstance(inputs, float | int):
                f = solve_Chebyshev(inputs)
                x_range = (-1, 1)
            else:
                f = solve_Euler(inputs[0], inputs[1])
                x_range = (0.01, 5)
            plot_function(f, is_dark, x_range)
            plot_latex(f, is_dark)
            self.combined_view.set_result()
        except Exception as e:
            print(f"runtime exception: {e}")
