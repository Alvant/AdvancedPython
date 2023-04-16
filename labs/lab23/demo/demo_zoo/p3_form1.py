import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QFormLayout,
    QLineEdit,
    QPushButton,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        # Another example of using flags.
        # Here we say that our window doesn't have default set of buttons,
        # but only minimize and close buttons.
        super().__init__(
            flags=(Qt.CustomizeWindowHint
                    | Qt.WindowMinimizeButtonHint
                    | Qt.WindowCloseButtonHint)
        )

        form = QFormLayout()
        form.addRow("Name:", QLineEdit())
        form.addRow("Age:", QLineEdit())

        button = QPushButton("OK")
        form.addRow(button)

        widget = QWidget()
        widget.setLayout(form)
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = MainWindow()
    w.setFixedWidth(200)
    w.show()

    app.exec()
