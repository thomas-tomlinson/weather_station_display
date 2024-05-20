from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QPainter, QPolygon, QFont, QFontMetrics, QPen, QColor
from PyQt6.QtWidgets import QApplication
import sys, time

class TimeProcess(QtCore.QObject):
    timedate = pyqtSignal(str)

    def __init__(self):
        QtCore.QThread.__init__(self)
        self.timer = QtCore.QTimer(self)
        self.running = True
        self.signal = pyqtSignal(str)

    def start_process(self):
        self.do_it()
        self.timer.timeout.connect(self.do_it)
        self.timer.start(1000)

    def do_it(self):
        time_string = time.strftime('%a %b %d %Y\n%H:%M:%S')
        self.timedate.emit(time_string)
        
    def stop(self):
        self._isRunning = False

class TimeInfo(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super(TimeInfo, self).__init__(*args, **kwargs)
        # init our values, place holders currently
        self._datetime = time.ctime()
        self._suninfo = '0800 / 2130'

        layout = QtWidgets.QVBoxLayout()

        self._time_label = QtWidgets.QLabel()
        self._time_label.setObjectName('time_label')
        layout.addWidget(self._time_label)
        self._time_values = QtWidgets.QLabel()
        self._time_values.setWordWrap(True)
        layout.addWidget(self._time_values)
        self._suninfo_label = QtWidgets.QLabel()
        self._suninfo_label.setObjectName('suninfo_label')
        layout.addWidget(self._suninfo_label)
        self._suninfo_values = QtWidgets.QLabel()
        layout.addWidget(self._suninfo_values)

        self.setLayout(layout) 
        self.init_labels()

        self.thread = QtCore.QThread(self)
        self.timei = TimeProcess()
        self.timei.timedate.connect(self.update_clock)
        self.timei.moveToThread(self.thread)
        self.thread.started.connect(self.timei.start_process)  
        self.thread.start()

        #self.update_values()
    @QtCore.pyqtSlot(str)
    def update_clock(self, value):
        self._time_values.setText("{}".format(value))

    #def mousePressEvent(self, event):
    #    self._datetime = time.ctime()
    #    self.update_values()

    def init_labels(self):
        # headers
        font = self.font()
        font.setPointSize(10)
        self._time_label.setFont(font)
        self._time_label.setText('CURRENT TIME')
        self._suninfo_label.setFont(font)
        self._suninfo_label.setText('SUNRISE / SUNSET')
        # time small
        font.setPointSize(20)
        self._time_values.setFont(font)
        
        #large data display
        font.setPointSize(50)
        self._suninfo_values.setFont(font)

    def update_values(self):
        self._time_values.setText("{}".format(self._datetime))
        self._suninfo_values.setText("{}".format(self._suninfo))

    def closeEvent(self, event):
        self.timei.stop()
        self.thread.quit()
        self.thread.wait()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    example = TimeInfo()
    example.show()
    app.exec()