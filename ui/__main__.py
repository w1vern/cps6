from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow
import sys
from PySide6.QtGui import QPalette, QColor


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
    app = QApplication(sys.argv)
    #set_light_palette(app)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
