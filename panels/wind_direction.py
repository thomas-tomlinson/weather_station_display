from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
import sys

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
        self._values = {}
        self._values['windDir'] = 0

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

        # wind direction
        windir = int(self._values['windDir'])

        #the pointer
        painter.save()
        painter.rotate(windir)
        center = QtCore.QRect(0, 0, 200, 200)
        painter.drawPolygon(
            QtGui.QPolygon([QtCore.QPoint(-5, -25), QtCore.QPoint(0, -45), QtCore.QPoint(5, -25),
                      QtCore.QPoint(0, -30), QtCore.QPoint(-5, -25)])
            )
        painter.restore()
        # wind direction text
        painter.save()
        value_offset = int(metrics.horizontalAdvance(str(windir))/2.0)
        painter.drawText(-value_offset, 0, str(windir))
        painter.restore()

        painter.end()

    def _trigger_refresh(self):
        self.update()

    #def setValue(self, value):
    #    self._value = value
    #    self.update()

    @QtCore.pyqtSlot(object)
    def setValue(self, object):
        # check for valid data and update as needed
        values_to_check = ['windSpeed_mph', 'windGust_mph', 'windDir']
        for value in values_to_check:
            if value in object:
                self._values[value] = float(object[value])
        self.update()

class WindDirection(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super(WindDirection, self).__init__(*args, **kwargs)

        self._values = {}
        self._values['windSpeed_mph'] = 0.0
        self._values['windGust_mph'] = 0.0

        layout = QtWidgets.QVBoxLayout()
        header_layout = QtWidgets.QHBoxLayout()
        self._compass = _Compass()

        #self._text = QtWidgets.QLabel()
        self._windspeed_label = QtWidgets.QLabel()
        self._windspeed_label.setText("A:")
        self._windspeed_label.setObjectName("windspeed_label")
        self._windspeed_label.setProperty('type', 'heading')
        header_layout.addWidget(self._windspeed_label)
        self._windspeed_value = QtWidgets.QLabel()
        header_layout.addWidget(self._windspeed_value)
        self._windgust_label = QtWidgets.QLabel()
        self._windgust_label.setText("G:")
        self._windgust_label.setObjectName("windgust_label")
        self._windgust_label.setProperty('type', 'heading')
        header_layout.addWidget(self._windgust_label)
        self._windgust_value = QtWidgets.QLabel()
        header_layout.addWidget(self._windgust_value)

        layout.addLayout(header_layout)
        layout.addWidget(self._compass)
        self.update_label()
        self.setLayout(layout)


    @QtCore.pyqtSlot(object)
    def setValue(self, object):
        # Compass setValue call
        self._compass.setValue(object)
        # local values processing for QLabel
        values_to_check = ['windSpeed_mph', 'windGust_mph']
        for value in values_to_check:
            if value in object:
                self._values[value] = float(object[value])
        self.update_label()

    def update_label(self):
        #self._text.setText("A: {:2.1f} G: {:2.1f} ".format(self._values['windSpeed_mph'], self._values['windGust_mph']))
        self._windspeed_value.setText("{:2.1f}".format(self._values['windSpeed_mph']))
        self._windgust_value.setText("{:2.1f}".format(self._values['windGust_mph']))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    example = WindDirection()
    example.show()
    app.exec()