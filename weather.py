#! /usr/bin/env python3
 
from bs4 import BeautifulSoup as bs
import os
import requests, json, re, sys
from time import strftime, ctime
from PyQt6.QtCore import (Qt, QTimer, QTime, pyqtSignal, pyqtSlot, QEvent)
from PyQt6.QtGui import (QImage, QPixmap, QFontDatabase, QFont)
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QGridLayout, QSizePolicy)
from PyQt6 import QtWidgets, QtCore, uic
#from MainWindow import Ui_MainWindow
from panels.bar_rainfall import BarRainfall
from panels.temp_humidity import TempHumidity
from panels.time_info import TimeInfo
from panels.wind_direction import WindDirection
from panels.graph import Graph
from panels.sat_image import SatImage
import paho.mqtt.client as mqtt
import weather_config.weather_config as wc


class MqttListener(QtCore.QObject):
    data = pyqtSignal(dict)
    def __init__(self):
        QtCore.QThread.__init__(self)
        self.timer = QtCore.QTimer(self)
        self.running = True
        self.signal = pyqtSignal(object)
        self.data_holder = {}

    def on_connect(self, client, userdata, flags, rc):
        print("Connect with result code " + str(rc))
        client.subscribe("weather_feed/loop")

    def on_message(self, client, userdata, msg):
        payload = json.loads(msg.payload.decode())
        # populate the data_holder and then emit it 
        for item in payload:
            self.data_holder[item] = payload[item]
                                             
        self.data.emit(self.data_holder)

    def start_process(self):
        self.do_it()

    def do_it(self):
        client = mqtt.Client()
        client.on_connect = self.on_connect
        client.on_message = self.on_message

        client.connect(wc.cfg['weewx_host'], 1883, 60)
        client.loop_forever()

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
        
        #font.setStretch(90)
        #self.setFont(font)
        self.layout = QGridLayout()
        self.layout.setVerticalSpacing(0)
        self.layout.setHorizontalSpacing(0)
        self.container = QWidget()
        size_policy = QSizePolicy()
        self.container.setSizePolicy(size_policy)
        self.container.setMinimumSize(QtCore.QSize(800, 480))
        self.container.setMaximumSize(QtCore.QSize(800, 480))
        self.setCentralWidget(self.container)


        bar_rain = BarRainfall()
        bar_rain.installEventFilter(self)
        #bar_rain.setMinimumWidth(200)
        temp_hum = TempHumidity()
        temp_hum.installEventFilter(self)
        #temp_hum.setMaximumHeight(180)
        time_info = TimeInfo()
        time_info.installEventFilter(self)
        #time_info.setMinimumWidth(300)
        wind_dir = WindDirection()
        wind_dir.installEventFilter(self)
        #wind_dir.setMinimumWidth(200)
        #self.sat_image = QtWidgets.QLabel()
        #self.sat_image.setScaledContents(True)
        sat_image = SatImage()
        sat_image.installEventFilter(self)
        #self.sat_image.setMinimumSize(300,300)
        graph = Graph()
        graph.installEventFilter(self)

        self.layout.addWidget(temp_hum, 0, 0)
        self.layout.addWidget(sat_image, 1, 0)
        self.layout.addWidget(wind_dir, 0, 1)
        self.layout.addWidget(bar_rain, 1, 1)
        self.layout.addWidget(time_info, 0, 2)
        self.layout.addWidget(graph, 1, 2)
        # sizing
        #layout.setColumnMinimumWidth(0, 300)
        self.layout.setColumnMinimumWidth(1, 200)
        #layout.setColumnMinimumWidth(2, 300)

        self.container.setLayout(self.layout)

        self.thread = QtCore.QThread(self)
        self.mqtt = MqttListener()
        self.mqtt.data.connect(temp_hum.setValue)
        self.mqtt.data.connect(bar_rain.setValue)
        self.mqtt.data.connect(wind_dir.setValue)
        self.mqtt.moveToThread(self.thread)
        self.thread.started.connect(self.mqtt.start_process)  
        self.thread.start()

    #def mouseDoubleClickEvent(self, event):
    def widgetResize(self):
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
            print(event)
            self.object_dbl_clicked = obj
            self.widgetResize()
        return False

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
