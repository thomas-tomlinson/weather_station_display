from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt, QRect
from PyQt6.QtGui import QPainter, QPolygon, QFont, QFontMetrics, QPen, QColor, QStaticText, QTextItem
from PyQt6.QtWidgets import QApplication
import sys

class TempHumidity(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super(TempHumidity, self).__init__(*args, **kwargs)
        # init our values
        self._inside_temp = 0.0
        self._inside_humidity = 0.0
        self._outide_temp = 0.0
        self._outside_humidity = 0.0

    def paintEvent(self, event):
        painter = QPainter(self)
        side = min(painter.device().width(), painter.device().height())
        #side = side - 2
        #painter.translate(painter.device().width() / 2, painter.device().height() / 2)
        #painter.scale(side / 200.0, side / 200.0)

        small_title_font = QtGui.QFont()
        small_title_font.setPixelSize(10)
        small_metrics = QtGui.QFontMetrics(small_title_font)
        
        large_whole_number_font = QtGui.QFont()
        large_whole_number_font.setPixelSize(90)
        large_metrics = QtGui.QFontMetrics(large_whole_number_font)

        medium_dec_number_font = QtGui.QFont()
        medium_dec_number_font.setPixelSize(20)
        medium_metrics = QtGui.QFontMetrics(medium_dec_number_font)

        painter.save()
        rect = QRect(0, 0, 20, 20)
        painter.setFont(small_title_font)
        #painter.drawText(0, (-100 + small_metrics.height()), "IN")
        painter.drawText(rect, 0, "IN")
        painter.drawRect(rect)
        painter.restore()

        display = '123.33F 99%'
        rect = QRect(0, 0, 300, 90)
        #real_sx = rect.width() * 1.0 / large_metrics.horizontalAdvance(display)
        #real_sy = rect.width() * 1.0 / large_metrics.height()
        #print(('width: {}, height: {}').format(large_metrics.horizontalAdvance(display), large_metrics.height()))
        #print(('real_sx: {}, real_sy: {}').format(real_sx, real_sy))
        painter.save()
        painter.drawRect(rect)
        painter.setFont(large_whole_number_font)
        #painter.translate(rect.center())
        #painter.scale(real_sx, real_sy)
        #painter.translate(-rect.center())
        painter.drawText(rect, 0, display)
        painter.restore()

        #painter.setFont(large_whole_number_font)
        #painter.drawText(rect, 0, '123.33F')

        #painter.drawStaticText(rect.topLeft(), text)
        #painter.setFont(medium_dec_number_font)

        #painter.drawText((-100 + large_metrics.horizontalAdvance("112.")), -70, "12")
        #painter.drawText(10, 10, "12")

        rect = QRect(0, 90, 20, 20)
        painter.setFont(small_title_font)
        #painter.drawText(0, (-100 + small_metrics.height()), "IN")
        painter.drawText(rect, 0, "OUT")
        painter.drawRect(rect)
        rect = QRect(0, 90, 300, 90)
        large_whole_number_font.setPixelSize(rect.height())
        painter.setFont(large_whole_number_font)
        painter.drawRect(rect)
        painter.drawText(rect, 0, '999.33F')

        painter.end()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    example = TempHumidity()
    example.show()
    app.exec()