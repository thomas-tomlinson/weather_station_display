from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QPainter, QPolygon, QFont, QFontMetrics, QPen, QColor, QPixmap, QImage
from PyQt6.QtWidgets import QApplication
import sys, time, json, requests, os


class FetchAlmanacData(QtCore.QObject):
    almanacData = pyqtSignal(object)
    def __init__(self):
        QtCore.QThread.__init__(self)
        self.timer = QtCore.QTimer(self)
        self.running = True
        self.signal = pyqtSignal(object)

    def start_process(self):
        self.do_it()
        self.timer.timeout.connect(self.do_it)
        self.timer.start(3600000)

    def do_it(self):
        data = {}
        try:
            raw_data = requests.get('http://weewx01.localdomain/belchertown/json/weewx_data.json')
            data = json.loads(raw_data.content)        
        except Exception as e:
            print("failed to query weewx_data.json from weewx host")

        try: 
            self.almanacData.emit(data['almanac'])
        except KeyError:
            # no data to emit
            print("failed to find the almanac key")
            pass
        
    def stop(self):
        self._isRunning = False

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

        hbox = QtWidgets.QHBoxLayout()
        gridLayout = QtWidgets.QGridLayout()
        gridLayout.setColumnStretch(2, 1)
        self._sunrise_image = QtWidgets.QLabel()
        gridLayout.addWidget(self._sunrise_image, 0, 0)
        self._sunset_image = QtWidgets.QLabel()
        gridLayout.addWidget(self._sunset_image, 1, 0)
        self._sunrise_value = QtWidgets.QLabel()
        gridLayout.addWidget(self._sunrise_value, 0, 1)
        self._sunset_value = QtWidgets.QLabel()
        gridLayout.addWidget(self._sunset_value, 1, 1)
        hbox.addLayout(gridLayout)

        self._moon_value = QtWidgets.QLabel()
        hbox.addWidget(self._moon_value)

        layout.addLayout(hbox)
        self.setLayout(layout) 
        self.init_labels()

        # clock thread
        self.thread = QtCore.QThread(self)
        self.timei = TimeProcess()
        self.timei.timedate.connect(self.update_clock)
        self.timei.moveToThread(self.thread)
        self.thread.started.connect(self.timei.start_process)  
        self.thread.start()

        # almanac data thread
        self.thread = QtCore.QThread(self)
        self.almanac = FetchAlmanacData()
        self.almanac.almanacData.connect(self.update_almanac)
        self.almanac.moveToThread(self.thread)
        self.thread.started.connect(self.almanac.start_process)  
        self.thread.start()

    @QtCore.pyqtSlot(str)
    def update_clock(self, value):
        self._time_values.setText("{}".format(value))

    @QtCore.pyqtSlot(object)
    def update_almanac(self, value):
        self._sunrise_value.setText("{}:{}".format(
            value['sunrise_hour'],
            value['sunrise_minute'],
            ))
        self._sunset_value.setText("{}:{}".format(
            value['sunset_hour'],
            value['sunset_minute'],
            ))
        moon_phase = value['moon']['moon_phase'].split()
        self._moon_value.setText("Moon:{}%\n{}\n{}".format(
            value['moon']['moon_fullness'],
            moon_phase[0],
            moon_phase[1],
            ))

    def init_labels(self):
        # headers
        font = self.font()
        font.setPointSize(10)
        self._time_label.setFont(font)
        self._time_label.setText('CURRENT TIME')
        self._suninfo_label.setFont(font)
        self._suninfo_label.setText('SUN AND MOON ')
        # time small
        font.setPointSize(20)
        self._time_values.setFont(font)
        
        #large data display
        #font.setPointSize(50)
        #self._suninfo_values.setFont(font)
        #self._suninfo_values.setFont(font)

        #images
        sunrise_image = QPixmap(os.path.join(os.path.dirname(__file__), '../images/sunrise.png'))
        self._sunrise_image.setPixmap(sunrise_image)
        sunset_image = QPixmap(os.path.join(os.path.dirname(__file__), '../images/sunset.png'))
        self._sunset_image.setPixmap(sunset_image)

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