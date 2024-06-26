from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QPolygon, QFont, QFontMetrics, QPen, QColor, QPalette
from PyQt6.QtWidgets import QApplication
import sys

class TempHumidity(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super(TempHumidity, self).__init__(*args, **kwargs)
        # init our values
        self._values = {}
        self._values['inTemp_F'] = 99.9
        self._values['outTemp_F'] = 99.9
        self._values['inHumidity'] = 0.0
        self._values['outHumidity'] = 0.0

        #layout = QtWidgets.QVBoxLayout()
        layout = QtWidgets.QGridLayout()
        layout.setColumnMinimumWidth(1, 5)
        layout.setHorizontalSpacing(0)
        layout.setVerticalSpacing(0)
        self._in_label = QtWidgets.QLabel()
        self._in_label.setObjectName("in_label")
        layout.addWidget(self._in_label, 0, 0)
        self._in_values = QtWidgets.QLabel()
        layout.addWidget(self._in_values, 0, 2)
        self._out_label = QtWidgets.QLabel()
        self._out_label.setObjectName("out_label")
        layout.addWidget(self._out_label, 1, 0)
        self._out_values = QtWidgets.QLabel()
        layout.addWidget(self._out_values, 1, 2)

        self.setLayout(layout) 
        self.init_labels()
        self.update_values()
    
    def init_labels(self):
        font = self.font()
        font.setPointSize(40)
        # headers
        self._in_label.setFont(font)
        self._in_label.setText('InSide')
        self._out_label.setFont(font)
        self._out_label.setText('OutSide')

        #large data display
        font.setPointSize(40)
        self._in_values.setFont(font)
        self._out_values.setFont(font)

    def update_values(self):
        self._in_values.setText("{:3.1f}F {:2.1f}%".format(self._values['inTemp_F'], self._values['inHumidity']))
        self._out_values.setText("{:3.1f}F {:2.1f}%".format(self._values['outTemp_F'], self._values['outHumidity']))

    @QtCore.pyqtSlot(object)
    def setValue(self, object):
        # check for valid data and update as needed
        values_to_check = ['inTemp_F', 'outTemp_F', 'inHumidity', 'outHumidity'] 
        for value in values_to_check:
            if value in object:
                self._values[value] = float(object[value])
        self.update_values()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    example = TempHumidity()
    example.show()
    app.exec()