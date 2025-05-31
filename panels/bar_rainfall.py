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
        self._values['barometer_inHg'] = 0.0
        self._values['rain24_in'] = 0.0

        layout = QtWidgets.QVBoxLayout()

        bar_hum_box = QtWidgets.QGridLayout()
        self._bar_label = QtWidgets.QLabel()
        self._bar_label.setObjectName('bar_label')
        self._bar_label.setProperty('type', 'heading')
        bar_hum_box.addWidget(self._bar_label, 0, 0)
        self._rain_label = QtWidgets.QLabel()
        self._rain_label.setObjectName('rain_label')
        self._rain_label.setProperty('type', 'heading')
        bar_hum_box.addWidget(self._rain_label, 0, 1)
        self._bar_values = QtWidgets.QLabel()
        bar_hum_box.addWidget(self._bar_values, 1, 0)
        self._rain_values = QtWidgets.QLabel()
        bar_hum_box.addWidget(self._rain_values, 1, 1)
        layout.addLayout(bar_hum_box)

        forecast_box = QtWidgets.QGridLayout()
        self._forecast_label = QtWidgets.QLabel()
        self._forecast_label.setProperty('type', 'heading')
        forecast_box.addWidget(self._forecast_label, 0, 0, 1, 0, alignment=Qt.AlignmentFlag.AlignCenter)
        self._forecast_hi_value = QtWidgets.QLabel()
        forecast_box.addWidget(self._forecast_hi_value, 1, 0)
        self._forecast_lo_value = QtWidgets.QLabel()
        forecast_box.addWidget(self._forecast_lo_value, 2, 0)
        self._forecast_text_value = QtWidgets.QLabel()
        forecast_box.addWidget(self._forecast_text_value, 1, 1, 0, 1)
        layout.addLayout(forecast_box)

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

        self._forecast_label.setFont(font)
        self._forecast_label.setText('FORECAST')

        #large data display
        font.setPointSize(40)
        self._bar_values.setFont(font)
        self._rain_values.setFont(font)

    def update_values(self):
        self._bar_values.setText("{:3.2f} inHg ".format(self._values['barometer_inHg']))
        self._rain_values.setText("{:2.2f} in".format(self._values['rain24_in']))

    @QtCore.pyqtSlot(object)
    def setValue(self, object):
        # check for valid data and update as needed
        values_to_check = ['barometer_inHg', 'rain24_in']
        for value in values_to_check:
            if value in object:
                self._values[value] = float(object[value])
        self.update_values()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    example = BarRainfall()
    example.show()
    app.exec()