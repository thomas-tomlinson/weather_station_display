from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt


class _Compass(QtWidgets.QWidget):
    clickedValue = QtCore.pyqtSignal(int)

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


    def sizeHint(self):
        return QtCore.QSize(120, 120)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        side = min(painter.device().width(), painter.device().height())
        painter.translate(painter.device().width() / 2, painter.device().height() / 2)
        painter.scale(side / 200.0, side / 200.0)


        #painter = QtGui.QPainter(self)
        brush = QtGui.QBrush()
        brush.setColor(QtGui.QColor('black'))
        #box_width = (painter.device().width() - 5)
        #box_height = (painter.device().height() - 5)
        rect = QtCore.QRect(-100, -100, 200, 200)
        #rect = QtCore.QRect(0, 0, 100, 100)
        painter.drawEllipse(rect)
        #painter.drawEllipse(0, 0, 100, 100)
        #painter.translate(50, 50)
        #painter.translate((box_width / 2), (box_height / 2))
        painter.save()
        i = 0
        while i < 360:
        
            if i % 45 == 0:
                painter.drawLine(0, -92, 0,-100)
                painter.drawText(0, -70, self._pointText[i])
                #painter.drawLine(0, 0, 0, -5)
                #painter.drawLine(0, (box_height / 2), 0, (box_height /2 ) - 5)
            else:
                #painter.drawLine(0, (box_height / 2), 0, (box_height /2 ) - 5)
                painter.drawLine(0, -95, 0, -100)
                #painter.drawLine(0, 0, 0, -5)
                #painter.drawLine(0, 50, 0, 45)
            painter.rotate(15)
            i += 15 
        painter.restore()

        spinbox = self.parent()._spinbox
        value = spinbox.value()

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
        painter.drawText(center, 0, str(value))
        painter.restore()
        painter.end()

    def _trigger_refresh(self):
        self.update()

class WindDirection(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super(WindDirection, self).__init__(*args, **kwargs)

        layout = QtWidgets.QVBoxLayout()
        self._compass = _Compass()
        layout.addWidget(self._compass)

        self._spinbox = QtWidgets.QSpinBox()
        self._spinbox.setMaximum(359)
        layout.addWidget(self._spinbox)

        self.setLayout(layout)
        self._spinbox.valueChanged.connect(self._compass._trigger_refresh)
