from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QPolygon, QFont, QFontMetrics, QPen, QColor
from PyQt6.QtWidgets import QApplication
import sys

class BarRainfall(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super(BarRainfall, self).__init__(*args, **kwargs)
        # init our values
        self._values = {}
        self._values['altimeter_inHg'] = 0.0
        self._values['rain24_in'] = 0.0

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
        self._bar_values.setText("{:3.2f} inHg ".format(self._values['altimeter_inHg']))
        self._rain_values.setText("{:2.1f} in".format(self._values['rain24_in']))

    @QtCore.pyqtSlot(object)
    def setValue(self, object):
        # check for valid data and update as needed
        values_to_check = ['altimeter_inHg', 'rain24_in']
        for value in values_to_check:
            if value in object:
                self._values[value] = float(object[value])
        self.update_values()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    example = BarRainfall()
    example.show()
    app.exec()