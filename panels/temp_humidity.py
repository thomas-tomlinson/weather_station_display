from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QPolygon, QFont, QFontMetrics, QPen, QColor, QPalette
from PyQt6.QtWidgets import QApplication
import sys


class CustomLabel(QtWidgets.QLabel):
    def adjustFont(self):
        if self.parent():
            # if the widget has a parent, get the available width by computing the
            # available rectangle between the parent rectangle and the widget
            # geometry (logical AND)
            rect = self.parent().rect() & self.geometry()
            width = rect.width()
            height = rect.height()
        else:
            width = self.width()
            height = self.height()
        font = self.font()
        text = self.text()
        #print("width: {}, height: {}".format(width, height))
        if font.pixelSize() == -1:
            self.fontSizeType = 'point'
        else:
            self.fontSizeType = 'pixel'

        while True:
            # compute the text width with the current font size
            textWidth = QtGui.QFontMetrics(font).size(
                Qt.TextFlag.TextSingleLine, text).width()
            textHeight = QtGui.QFontMetrics(font).size(
                Qt.TextFlag.TextSingleLine, text).height()
            # break if the width is enough to show the text or the font size is
            # sufficient to keep the text readable
            #print('text width: {}, text height: {} font size type: {}'.format(textWidth, textHeight, self.fontSizeType))
            #if textWidth <= width or font.pixelSize() <= 6:
            if textWidth <= width:
                #scale up
                self._changeFontSize('bigger', font)
            #elif textWidth > width:
            #    self._changeFontSize('smaller', font)
            else:
                break 
            #print("textWidth: {}, width: {}".format(textWidth, width))
        self._font = font

    def _changeFontSize(self, direction, font):
        if direction == 'bigger':
            if self.fontSizeType == 'pixel':
                font.setPixelSize(font.pixelSize() + 1)
            else:
                font.setPointSize(font.pointSize() + 1)
        elif direction == 'smaller':
            if self.fontSizeType == 'pixel':
                font.setPixelSize(font.pixelSize() - 1)
            else:
                font.setPointSize(font.pointSize() - 1)


    def setText(self, text):
        super().setText(text)
        self.adjustFont()

    def resizeEvent(self, event):
        self.adjustFont()

    def paintEvent(self, event):
        if self.text():
            qp = QtGui.QPainter(self)
            qp.setFont(self._font)
            qp.drawText(self.rect(), self.alignment(), self.text())
        else:
            super().paintEvent(event)

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
        #layout.setHorizontalSpacing(0)
        #layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)

       #layout.setVerticalSpacing(0)
        self._in_label = QtWidgets.QLabel()
        self._in_label.setObjectName("in_label")
        layout.addWidget(self._in_label, 0, 0)
        #self._in_values = QtWidgets.QLabel()
        self._in_values = CustomLabel()
        self._in_values.setObjectName("in_values")
        layout.addWidget(self._in_values, 0, 1)
        self._out_label = QtWidgets.QLabel()
        self._out_label.setObjectName("out_label")
        layout.addWidget(self._out_label, 1, 0)
        #self._out_values = QtWidgets.QLabel()
        self._out_values = CustomLabel()
        self._out_values.setObjectName("out_values")
        layout.addWidget(self._out_values, 1, 1)

        self.setLayout(layout) 
        self.init_labels()
        self.update_values()
    
    def init_labels(self):
        font = self.font()
        font.setPointSize(20)
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