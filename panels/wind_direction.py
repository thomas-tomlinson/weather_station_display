from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt


class _Compass(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.MinimumExpanding,
            QtWidgets.QSizePolicy.Policy.MinimumExpanding,
        )

        self._bar_solid_percent = 0.8
        self._background_color = QtGui.QColor('black')
        self._padding = 4.0
        self._pointText = {0: "N", 45: "NE", 90: "E", 135: "SE", 180: "S",
            225: "SW", 270: "W", 315: "NW"}
        #initialize the value 
        self._value = 0


    def sizeHint(self):
        return QtCore.QSize(120, 120)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        side = min(painter.device().width(), painter.device().height())
        side = side - 2
        painter.translate(painter.device().width() / 2, painter.device().height() / 2)
        painter.scale(side / 200.0, side / 200.0)


        brush = QtGui.QBrush()
        brush.setColor(QtGui.QColor('black'))
        rect = QtCore.QRect(-100, -100, 200, 200)
        painter.drawEllipse(rect)


        font = QtGui.QFont()
        font.setPixelSize(20)
        metrics = QtGui.QFontMetrics(font)
        painter.setFont(font)
        painter.save()
        i = 0
        while i < 360:
        
            if i % 45 == 0:
                painter.drawLine(0, -92, 0,-100)
                text_center_offset = int(metrics.horizontalAdvance(self._pointText[i])/2.0)
                painter.drawText(-text_center_offset, -70, self._pointText[i])
            else:
                painter.drawLine(0, -95, 0, -100)
            painter.rotate(15)
            i += 15 
        painter.restore()

        value = self._value

        #the pointer
        painter.save()
        painter.rotate(value)
        center = QtCore.QRect(0, 0, 200, 200)
        painter.drawPolygon(
            QtGui.QPolygon([QtCore.QPoint(-5, -25), QtCore.QPoint(0, -45), QtCore.QPoint(5, -25),
                      QtCore.QPoint(0, -30), QtCore.QPoint(-5, -25)])
            )
        painter.restore()
        painter.save()
        value_offset = int(metrics.horizontalAdvance(str(value))/2.0)
        painter.drawText(-value_offset, 0, str(value))
        painter.restore()
        painter.end()

    def _trigger_refresh(self):
        self.update()

    def setValue(self, value):
        self._value = value
        self.update()

class WindDirection(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super(WindDirection, self).__init__(*args, **kwargs)

        layout = QtWidgets.QVBoxLayout()
        self._compass = _Compass()
        layout.addWidget(self._compass)

        self.setLayout(layout)

    @QtCore.pyqtSlot(int)
    def setValue(self, value):
        self._compass.setValue(value)

