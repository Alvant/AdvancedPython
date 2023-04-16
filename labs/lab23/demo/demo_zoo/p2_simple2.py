import sys

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QHBoxLayout,
    QLabel,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        label1 = QLabel("Hello World!")
        label2 = QLabel("Have a nice day!")
        layout.addWidget(label1)
        layout.addWidget(label2)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.setFixedWidth(200)
    window.show()

    app.exec()
