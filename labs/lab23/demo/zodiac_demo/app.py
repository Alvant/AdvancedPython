import os
import sys

from datetime import datetime, date

from PyQt5 import QtCore
from PyQt5.QtCore import (
    Qt,
    pyqtSlot,
    pyqtSignal,
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QFormLayout,
    QLineEdit,
    QComboBox,
    QPushButton,
    QWidget,
    QMessageBox,
)


_SOME_LEAP_YEAR = 1992

_MONTH_TO_NDAYS = {
    'Январь': 31,
    'Февраль': 29,
    'Март': 31,
    'Апрель': 30,
    'Май': 31,
    'Июнь': 30,
    'Июль': 31,
    'Август': 31,
    'Сентябрь': 30,
    'Октябрь': 31,
    'Ноябрь': 30,
    'Декабрь': 31,
}

_MONTH_TO_NUMBER = {
    month: number
    for month, number in zip(_MONTH_TO_NDAYS, range(1, len(_MONTH_TO_NDAYS) + 1))
}


class MainWindow(QMainWindow):
    processed = pyqtSignal(str, str)

    def __init__(self, zodiac_folder='zodiac_images'):
        super().__init__(flags=Qt.CustomizeWindowHint | Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)

        layout = QFormLayout()

        self.name = QLineEdit()
        self.month = QComboBox()
        self.month.addItems(
            [''] + list(_MONTH_TO_NDAYS.keys())
        )

        self.day = QComboBox()

        layout.addRow("Name:", self.name)
        layout.addRow("Month of birth:", self.month)
        layout.addRow("Day of birth:", self.day)

        self.month.activated.connect(self.on_activated)

        button = QPushButton("OK")
        button.pressed.connect(self.on_pressed)
        layout.addRow(button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.processed.connect(self.on_processed)

        self._zodiac_images_folder = zodiac_folder
        current_date = datetime.now().date()
        self._reference_date = date(
            _SOME_LEAP_YEAR, current_date.month, current_date.day
        )

    @pyqtSlot(int)
    def on_activated(self, index):
        # TODO: remove empty month option if one is selected

        if self.month.currentText() == '':
            num_days = 0
        else:
            num_days = _MONTH_TO_NDAYS[self.month.currentText()]

        while self.day.count() > num_days:
            self.day.removeItem(self.day.count() - 1)

        while self.day.count() < num_days:
            if self.day.count() == 0:
                previous_day = 0
            else:
                previous_day = int(self.day.itemText(self.day.count() - 1))

            self.day.addItem(str(previous_day + 1))

    @pyqtSlot()
    def on_pressed(self):
        res = f"Hello, {self.name.text()}."

        if self.month.currentText() == '' or self.day.currentText() == '':
            image_file_name = None
        else:
            month = _MONTH_TO_NUMBER[self.month.currentText()]
            day = int(self.day.currentText())
            image_file_name = self._get_zodiac_image(month=month, day=day)
            zodiac_name = os.path.splitext(image_file_name)[0]
            zodiac_name = zodiac_name[0].upper() + zodiac_name[1:]
            res += '\n' + f"Your zodiac sign is {zodiac_name}."

        self.processed.emit(res, image_file_name)

    @pyqtSlot(str, str)
    def on_processed(self, info, image_file_name=None):
        msg = QMessageBox(self)

        if image_file_name is None:
            pass
        else:
            image_path = os.path.join(self._zodiac_images_folder, image_file_name)
            pixmap = QPixmap(image_path)
            pixmap = pixmap.scaled(100, 100, Qt.KeepAspectRatio)
            msg.setIconPixmap(pixmap)

        msg.setText(info)
        msg.setWindowTitle("Welcome")
        msg.exec()

    def _get_zodiac_image(self, month: int, day: int) -> str:
        some_year = self._reference_date.year
        input_date = date(some_year, month, day)

        if date(some_year, 3, 21) <= input_date <= date(some_year, 4, 20):
            image_name = 'aries.png'
        elif date(some_year, 4, 21) <= input_date <= date(some_year, 5, 21):
            image_name = 'taurus.png'
        elif date(some_year, 5, 22) <= input_date <= date(some_year, 6, 21):
            image_name = 'gemini.png'
        elif date(some_year, 6, 22) <= input_date <= date(some_year, 7, 22):
            image_name = 'cancer.png'
        elif date(some_year, 7, 23) <= input_date <= date(some_year, 8, 23):
            image_name = 'leo.png'
        elif date(some_year, 8, 24) <= input_date <= date(some_year, 9, 22):
            image_name = 'virgo.png'
        elif date(some_year, 9, 23) <= input_date <= date(some_year, 10, 23):
            image_name = 'libra.png'
        elif date(some_year, 10, 24) <= input_date <= date(some_year, 11, 22):
            image_name = 'scorpio.png'
        elif date(some_year, 11, 23) <= input_date <= date(some_year, 12, 21):
            image_name = 'sagittarius.png'
        elif date(some_year, 12, 22) <= input_date <= date(some_year + 1, 1, 20):  # + 1 year for the two-side comparison
            image_name = 'capricorn.png'
        elif date(some_year, 1, 21) <= input_date <= date(some_year, 2, 18):
            image_name = 'aquarius.png'
        elif date(some_year, 2, 19) <= input_date <= date(some_year, 3, 20):
            image_name = 'pisces.png'

        return image_name


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("""
        QLabel{font-size: 18pt;}
        QLineEdit{font-size: 18pt;}
        QComboBox{font-size: 18pt;}
    """)

    w = MainWindow()
    w.setFixedWidth(350)
    w.show()

    app.exec()
