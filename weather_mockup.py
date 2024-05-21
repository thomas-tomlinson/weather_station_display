#! /usr/bin/env python3
 
from bs4 import BeautifulSoup as bs
import os
import requests, json, re, sys
from time import strftime, ctime
from PyQt6.QtCore import (Qt, QTimer, QTime, pyqtSignal, pyqtSlot, QEvent)
from PyQt6.QtGui import (QImage, QPixmap, QFontDatabase, QFont)
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QGridLayout, QSizePolicy,)
from PyQt6 import QtWidgets, QtCore, uic
#from MainWindow import Ui_MainWindow
from panels.bar_rainfall import BarRainfall
from panels.temp_humidity import TempHumidity
from panels.time_info import TimeInfo
from panels.wind_direction import WindDirection
from panels.graph import Graph

class PwsWeather(QtCore.QObject):
    data = pyqtSignal(dict)
    def __init__(self):
        QtCore.QThread.__init__(self)
        self.timer = QtCore.QTimer(self)
        self.running = True
        self.signal = pyqtSignal(object)

    def start_process(self):
        self.do_it()
        self.timer.timeout.connect(self.do_it)
        self.timer.start(180000)

    def do_it(self):
        #get the current pws weather live page
        page = requests.get('http://192.168.1.119/livedata.htm')
        soup = bs(page.text, 'html.parser')
        all_items = soup.find_all('input', attrs={'disabled':'disabled'})

        # data holder
        w_data = {}

        #find the data elements fron the horrific ambient weather live data
        for item in all_items:
            w_data[item["name"]] = item["value"]

        w_data['update_time'] = ctime()
        self.data.emit(w_data)

    def stop(self):
        self._isRunning = False

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__()

        # load font
        dirname, filename = os.path.split(os.path.abspath(__file__)) 
        load = QFontDatabase.addApplicationFont(dirname + '/fonts/OxygenMono-Regular.ttf')
        load = QFontDatabase.addApplicationFont(dirname + '/fonts/Audiowide-Regular.ttf')
        load = QFontDatabase.addApplicationFont(dirname + '/fonts/BrunoAce-Regular.ttf')
        #font = QFont('Oxygen Mono')
        with open('style.qss', 'r') as f:
            _style = f.read()
            self.setStyleSheet(_style)
        
        self.layout = QGridLayout()
        self.layout.setVerticalSpacing(0)
        self.layout.setHorizontalSpacing(0)
        self.container = QWidget()
        size_policy = QSizePolicy()
        self.container.setSizePolicy(size_policy)
        self.container.setMinimumSize(QtCore.QSize(800, 480))
        self.container.setMaximumSize(QtCore.QSize(800, 480))
        self.setCentralWidget(self.container)

        self.bar_rain = BarRainfall()
        self.bar_rain.installEventFilter(self)
        #bar_rain.setMinimumWidth(200)
        self.temp_hum = TempHumidity()
        self.temp_hum.installEventFilter(self)
        #temp_hum.setMaximumHeight(180)
        self.time_info = TimeInfo()
        self.time_info.installEventFilter(self)
        #time_info.setMinimumWidth(300)
        self.wind_dir = WindDirection()
        self.wind_dir.installEventFilter(self)
        #wind_dir.setMinimumWidth(200)
        self.sat_image = QtWidgets.QLabel()
        self.sat_image.setScaledContents(True)
        self.sat_image.installEventFilter(self)

        #self.sat_image.setMinimumSize(300,300)
        self.graph = Graph()
        self.graph.installEventFilter(self)
        self.layout.addWidget(self.temp_hum, 0, 0)
        self.layout.addWidget(self.sat_image, 1, 0)
        self.layout.addWidget(self.wind_dir, 0, 1)
        self.layout.addWidget(self.bar_rain, 1, 1)
        self.layout.addWidget(self.time_info, 1, 2)
        self.layout.addWidget(self.graph, 0, 2)
        # sizing
        #layout.setColumnMinimumWidth(0, 300)
        #layout.setColumnMinimumWidth(1, 200)
        #layout.setColumnMinimumWidth(2, 300)

        self.container.setLayout(self.layout)

        self.thread = QtCore.QThread(self)
        self.pws = PwsWeather()
        self.pws.data.connect(self.temp_hum.setValue)
        self.pws.data.connect(self.bar_rain.setValue)
        self.pws.data.connect(self.wind_dir.setValue)
        self.pws.moveToThread(self.thread)
        self.thread.started.connect(self.pws.start_process)  
        self.thread.start()
        self.update_sat_image()

    def mouseDoubleClickEvent(self, event):
        index = self.layout.count()
        hiddenCount = 0
        visibleCount = 0
        for i in range(index):
            widget = self.layout.itemAt(i).widget()
            if widget.isVisible() is True:
                visibleCount += 1
            else:
                hiddenCount += 1
        if visibleCount > hiddenCount:
            # assume all panels are visble, this is a call 
            # to full screen the doubleclicked one.
            for i in range(index):
                widget = self.layout.itemAt(i).widget()
                if widget != self.object_dbl_clicked:
                    widget.hide()
        else:
            # this assumes there's just one panel visible.
            # in which case we'll make everything visible
             for i in range(index):
                widget = self.layout.itemAt(i).widget()
                widget.show()

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.MouseButtonDblClick:
            self.object_dbl_clicked = obj
        return False

    def update_sat_image(self):
        image = QImage()
        try:
            sat_image_bitmap = requests.get('https://cdn.star.nesdis.noaa.gov/GOES18/ABI/SECTOR/pnw/GEOCOLOR/300x300.jpg').content
        except Exception as e:
            sat_image_bitmap = None
            print('failed to retrieve satellite image, error:', e)
        if sat_image_bitmap is not None:
            image.loadFromData(sat_image_bitmap)
            self.sat_image.setPixmap(QPixmap(image))



def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    #needed for X less raspberry pi
    #os.environ["QT_QPA_PLATFORM"] = "eglfs"
    #os.environ["QT_QPA_EGLFS_HIDECURSOR"] = "1"

    main()
