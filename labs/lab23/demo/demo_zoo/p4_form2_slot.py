import sys

from PyQt5.QtCore import (
    Qt,
    pyqtSlot,
)
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QFormLayout,
    QLineEdit,
    QSpinBox,
    QPushButton,
    QWidget,
    QMessageBox,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__(
            flags=(Qt.CustomizeWindowHint
                    | Qt.WindowMinimizeButtonHint
                    | Qt.WindowCloseButtonHint
            )
        )

        layout = QFormLayout()

        self.name = QLineEdit()
        self.email = QLineEdit()
        self.age = QSpinBox()
        self.age.setRange(0, 999)

        layout.addRow("Name:", self.name)
        layout.addRow("E-mail:", self.email)
        layout.addRow("Age:", self.age)

        button = QPushButton("OK")
        button.pressed.connect(self.on_pressed)       
        layout.addRow(button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def on_pressed(self):
        print(f"Hello, {self.name.text()}!")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = MainWindow()
    w.setFixedWidth(200)
    w.show()

    app.exec()
