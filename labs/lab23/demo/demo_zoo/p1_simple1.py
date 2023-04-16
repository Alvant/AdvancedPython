import sys

from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    label = QLabel("Hello World!")
    label.setFixedWidth(200)
    label.show()

    app.exec()
