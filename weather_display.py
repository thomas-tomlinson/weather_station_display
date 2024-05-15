#! /usr/bin/env python3
 
from bs4 import BeautifulSoup as bs
import os
import requests, json, re, sys
from time import strftime, ctime
from PyQt6.QtCore import (Qt, QTimer, QTime, pyqtSignal, pyqtSlot)
from PyQt6.QtGui import (QImage, QPixmap)
#from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QGridLayout,)
from PyQt6 import QtWidgets, QtCore, uic
from MainWindow import Ui_MainWindow


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

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.thread = QtCore.QThread(self)
        self.pws = PwsWeather()
        self.pws.data.connect(self.update_weather_data)
        self.pws.moveToThread(self.thread)
        self.thread.started.connect(self.pws.start_process)  
        self.thread.start()

        # add the initial satellite image 
        self.update_sat_image()

        # clock update time
        clock_update_timer = QTimer(self)
        clock_update_timer.timeout.connect(self.update_clock)
        clock_update_timer.start(1000)

        # Sat image update, every 30 minutes
        sat_update_timer = QTimer(self)
        sat_update_timer.timeout.connect(self.update_sat_image)
        sat_update_timer.start(1800000)

    def update_clock(self):
        self.cur_datetime.setText(ctime())

    def update_sat_image(self):
        image = QImage()
        try:
            sat_image = requests.get('https://cdn.star.nesdis.noaa.gov/GOES18/ABI/SECTOR/pnw/GEOCOLOR/300x300.jpg').content
        except Exception as e:
            sat_image = None
            print('failed to retrieve satellite image, error:', e)
        if sat_image is not None:
            image.loadFromData(sat_image)
            self.sat_image.setPixmap(QPixmap(image))

    def closeEvent(self, event):
        self.pws.stop()
        self.thread.quit()
        self.thread.wait()

    @QtCore.pyqtSlot(object)
    def update_weather_data(self, data):
        self.outside_f.setText(data['outTemp'] + '\u2109')
        self.inside_f.setText(data['inTemp'] + '\u2109') 
        self.outside_humidity.setText(data['outHumi'] + '%')
        self.inside_humidify.setText(data['inHumi'] + '%') 
        self.wind_direction.setValue(int(data['windir']))
        self.wind_speed.setText('avg: ' + data['avgwind'] + 'mph')
        self.wind_gust.setText('gust: ' + data['gustspeed'] + 'mph')
        self.rel_pressure.setText(data['RelPress'])


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
