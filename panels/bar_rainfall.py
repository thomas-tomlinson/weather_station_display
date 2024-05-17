from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QPolygon, QFont, QFontMetrics, QPen, QColor
from PyQt6.QtWidgets import QApplication
import sys

class BarRainfall(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super(BarRainfall, self).__init__(*args, **kwargs)
        # init our values
        self._barometer = '0.0'
        self._last24hour_rainfall = '0.0'

        layout = QtWidgets.QVBoxLayout()

        self._bar_label = QtWidgets.QLabel()
        self._bar_label.setObjectName('bar_label')
        layout.addWidget(self._bar_label)
        self._bar_values = QtWidgets.QLabel()
        layout.addWidget(self._bar_values)
        self._rain_label = QtWidgets.QLabel()
        self._rain_label.setObjectName('rain_label')
        layout.addWidget(self._rain_label)
        self._rain_values = QtWidgets.QLabel()
        layout.addWidget(self._rain_values)

        self.setLayout(layout) 
        self.init_labels()
        self.update_values()
    
    def init_labels(self):
        # headers
        font = self.font()
        font.setPointSize(10)
        self._bar_label.setFont(font)
        self._bar_label.setText('BAROMETER')
        self._rain_label.setFont(font)
        self._rain_label.setText('RAINFALL')

        #large data display
        font.setPointSize(40)
        self._bar_values.setFont(font)
        self._rain_values.setFont(font)

    def update_values(self):
        self._bar_values.setText("{} inHg ".format(self._barometer))
        self._rain_values.setText("{} in".format(self._last24hour_rainfall))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    example = BarRainfall()
    example.show()
    app.exec()