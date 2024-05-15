from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QPolygon, QFont, QFontMetrics, QPen, QColor
from PyQt6.QtWidgets import QApplication
import sys, time

class TimeInfo(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super(TimeInfo, self).__init__(*args, **kwargs)
        # init our values, place holders currently
        self._datetime = time.ctime()
        self._suninfo = '0800 / 2130'


        layout = QtWidgets.QVBoxLayout()

        self._time_label = QtWidgets.QLabel()
        layout.addWidget(self._time_label)
        self._time_values = QtWidgets.QLabel()
        layout.addWidget(self._time_values)
        self._suninfo_label = QtWidgets.QLabel()
        layout.addWidget(self._suninfo_label)
        self._suninfo_values = QtWidgets.QLabel()
        layout.addWidget(self._suninfo_values)

        self.setLayout(layout) 
        self.init_labels()
        self.update_values()
    
    def init_labels(self):
        # headers
        small_style_sheet = 'font-size: 10pt;'
        self._time_label.setStyleSheet(small_style_sheet)
        self._time_label.setText('CURRENT TIME')
        self._suninfo_label.setStyleSheet(small_style_sheet)
        self._suninfo_label.setText('SUNRISE / SUNSET')

        #large data display
        large_style_sheet = 'font-size: 50pt;'
        self._time_values.setStyleSheet(large_style_sheet)
        self._suninfo_values.setStyleSheet(large_style_sheet)

    def update_values(self):
        self._time_values.setText("{}".format(self._datetime))
        self._suninfo_values.setText("{}".format(self._suninfo))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    example = TimeInfo()
    example.show()
    app.exec()