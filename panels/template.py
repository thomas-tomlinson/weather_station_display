from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QPolygon, QFont, QFontMetrics, QPen, QColor
from PyQt6.QtWidgets import QApplication
import sys

class Example(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)



    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setPen(Qt.GlobalColor.red)
        rect = QtCore.QRect(0, 0, 200, 200)
        painter.drawRect(rect)
        painter.end()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    example = Example()
    example.show()
    app.exec()