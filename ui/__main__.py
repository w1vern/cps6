from PySide6.QtWidgets import QApplication
from sympy import plot
from ui.main_window import MainWindow
import sys
from PySide6.QtGui import QPalette, QColor
from plotter import plot_latex, plot_function
from solver import solve_Chebyshev

import os


def create_dir_and_file(directory_name: str, file_names: list[str]):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

    for file_name in file_names:
        file_path = os.path.join(directory_name, file_name)
        if not os.path.exists(file_path):
            f = solve_Chebyshev(1.)
            if file_name=="latex.svg":
                plot_latex(f, True)
            elif file_name=="function.svg":
                plot_function(f, True, (-1, 1))
            else:
                raise Exception("wrong file name")


            


def set_light_palette(app: QApplication):
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor("white"))
    palette.setColor(QPalette.ColorRole.WindowText, QColor("black"))
    palette.setColor(QPalette.ColorRole.Base, QColor("white"))
    palette.setColor(QPalette.ColorRole.AlternateBase, QColor("#f0f0f0"))
    palette.setColor(QPalette.ColorRole.ToolTipBase, QColor("white"))
    palette.setColor(QPalette.ColorRole.ToolTipText, QColor("black"))
    palette.setColor(QPalette.ColorRole.Text, QColor("black"))
    palette.setColor(QPalette.ColorRole.Button, QColor("#f0f0f0"))
    palette.setColor(QPalette.ColorRole.ButtonText, QColor("black"))
    palette.setColor(QPalette.ColorRole.BrightText, QColor("red"))
    palette.setColor(QPalette.ColorRole.Highlight, QColor("#3874f2"))
    palette.setColor(QPalette.ColorRole.HighlightedText, QColor("white"))

    app.setPalette(palette)


def main() -> None:
    create_dir_and_file("render", ["latex.svg", "function.svg"])
    app = QApplication(sys.argv)
    # set_light_palette(app)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
