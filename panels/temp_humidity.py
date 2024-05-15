from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QPolygon, QFont, QFontMetrics, QPen, QColor
from PyQt6.QtWidgets import QApplication
import sys

class TempHumidity(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super(TempHumidity, self).__init__(*args, **kwargs)
        # init our values
        self._inside_temp = '99.9'
        self._inside_humidity = '0.0'
        self._outside_temp = '99.9'
        self._outside_humidity = '0.0'

        layout = QtWidgets.QVBoxLayout()

        self._in_label = QtWidgets.QLabel()
        layout.addWidget(self._in_label)
        self._in_values = QtWidgets.QLabel()
        layout.addWidget(self._in_values)
        self._out_label = QtWidgets.QLabel()
        layout.addWidget(self._out_label)
        self._out_values = QtWidgets.QLabel()
        layout.addWidget(self._out_values)

        self.setLayout(layout) 
        self.init_labels()
        self.update_values()
    
    def init_labels(self):
        font = self.font()
        font.setPointSize(10)
        # headers
        self._in_label.setFont(font)
        self._in_label.setText('IN')
        self._out_label.setFont(font)
        self._out_label.setText('OUT')

        #large data display
        font.setPointSize(40)
        self._in_values.setFont(font)
        self._out_values.setFont(font)

    def update_values(self):
        self._in_values.setText("{}F {}%".format(self._inside_temp, self._inside_humidity))
        self._out_values.setText("{}F {}%".format(self._outside_temp, self._outside_humidity))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    example = TempHumidity()
    example.show()
    app.exec()