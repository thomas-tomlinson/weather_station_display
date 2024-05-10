#! /usr/bin/env python3
 
from bs4 import BeautifulSoup as bs
import os
import requests, json, re, sys
from time import strftime, ctime
from PyQt6.QtCore import (Qt, QTimer, QTime)
from PyQt6.QtGui import (QImage, QPixmap)
#from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QGridLayout,)
from PyQt6 import QtWidgets, QtCore, uic


class PwsWeather:
    def __init__(self):
        #get the current pws weather live page
        page = requests.get('http://192.168.1.119/livedata.htm')
        soup = bs(page.text, 'html.parser')
        all_items = soup.find_all('input', attrs={'disabled':'disabled'})

        # data holder
        self.data = {}

        #find the data elements fron the horrific ambient weather live data
        for item in all_items:
            self.data[item["name"]] = item["value"]

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Iniate the Weather class
        weather = PwsWeather()
        self.data = weather.data
        
        mw = uic.loadUi("mainwindow.ui", self)
        #mw.outside_f.setText(weather.data['outTemp'] + '\u2109')
        #mw.inside_f.setText(weather.data['inTemp'] + '\u2109') 
        #mw.outside_humidity.setText(weather.data['outHumi'] + '%')
        #mw.inside_humidify.setText(weather.data['inHumi'] + '%') 

        #mw.wind_direction.setText(weather.data['windir'] + '\u00ba')
        #mw.wind_speed.setText('avg: ' + weather.data['avgwind'] + 'mph')
        #mw.wind_gust.setText('gust: ' + weather.data['gustspeed'] + 'mph')

        #mw.rel_pressure.setText(weather.data['RelPress'])
        #mw.cur_datetime.setText(ctime())
        #i = 0
        #self.myvlabels = []
        #hlabels = []
        #for key, value in self.data.items():
        #    self.myvlabels.append(value)
        #    hlabels.append(key)
        #    hlabels[i] = QLabel(f'<b>{key}</b>:')
        #    hlabels[i].setStyleSheet('border: 1px solid lightgray; padding: 0 0 0 8;')
        #    self.myvlabels[i] = QLabel(value)
        #    self.myvlabels[i].setStyleSheet('border: 1px solid lightgray; padding 0 0 0 0;')
        #    layout.addWidget(hlabels[i], i, 0)
        #    layout.addWidget(self.myvlabels[i], i, 1)
        #    i += 1


        # add the sat image at the bottom
        image = QImage()
        image.loadFromData(requests.get('https://cdn.star.nesdis.noaa.gov/GOES18/ABI/SECTOR/pnw/GEOCOLOR/300x300.jpg').content)
        #img_label = QLabel()
        mw.sat_image.setPixmap(QPixmap(image))

        # clock update time
        clock_update_timer = QTimer(self)
        clock_update_timer.timeout.connect(self.update_clock)
        clock_update_timer.start(1000)

        # weather data update timer
        weather_update_timer = QTimer(self)
        weather_update_timer.timeout.connect(self.update_weather_data)
        weather_update_timer.start(30000)

    def update_clock(self):
        self.cur_datetime.setText(ctime())

    def update_weather_data(self):
        weather = PwsWeather()
        self.outside_f.setText(weather.data['outTemp'] + '\u2109')
        self.inside_f.setText(weather.data['inTemp'] + '\u2109') 
        self.outside_humidity.setText(weather.data['outHumi'] + '%')
        self.inside_humidify.setText(weather.data['inHumi'] + '%') 

        self.wind_direction.setText(weather.data['windir'] + '\u00ba')
        self.wind_speed.setText('avg: ' + weather.data['avgwind'] + 'mph')
        self.wind_gust.setText('gust: ' + weather.data['gustspeed'] + 'mph')

        self.rel_pressure.setText(weather.data['RelPress'])

    #def update(self):
    #    weather = PwsWeather()
    #    data = weather.data
    #    i = 0
    #    for val in data.values():
    #        self.myvlabels[i].setText(val)
    #        i += 1
    def mousePressEvent(self, e):
        print("mouse pressmove detected: ", e.button())

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
