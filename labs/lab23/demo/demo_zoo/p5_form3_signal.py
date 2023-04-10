import sys

from PyQt5.QtCore import (
    Qt,
    pyqtSlot,
    pyqtSignal,
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
    processed = pyqtSignal(str)

    def __init__(self):
        super().__init__(
            flags=(Qt.CustomizeWindowHint
                    | Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
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

        self.processed.connect(self.on_processed)

    @pyqtSlot()
    def on_pressed(self):
        result = (
            f"Your name is {self.name.text()}.\n"
            f"Your email is {self.email.text()}.\n"
            f"Your age is {self.age.text()}."
        )

        self.processed.emit(result)

    @pyqtSlot(str)
    def on_processed(self, info):
        msg = QMessageBox(self)
        msg.setText(info)
        msg.setWindowTitle("Welcome!")
        msg.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = MainWindow()
    w.setFixedWidth(200)
    w.show()

    app.exec()
