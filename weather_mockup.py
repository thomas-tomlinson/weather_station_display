#! /usr/bin/env python3
 
from bs4 import BeautifulSoup as bs
import os
import requests, json, re, sys
from time import strftime, ctime
from PyQt6.QtCore import (Qt, QTimer, QTime, pyqtSignal, pyqtSlot)
from PyQt6.QtGui import (QImage, QPixmap)
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QGridLayout, QSizePolicy)
from PyQt6 import QtWidgets, QtCore, uic
#from MainWindow import Ui_MainWindow
from panels.bar_rainfall import BarRainfall
from panels.temp_humidity import TempHumidity
from panels.time_info import TimeInfo
from panels.wind_direction import WindDirection



class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__()

        layout = QGridLayout()
        layout.setVerticalSpacing(0)
        layout.setHorizontalSpacing(0)
        self.container = QWidget()
        size_policy = QSizePolicy()
        self.container.setSizePolicy(size_policy)
        self.container.setMinimumSize(QtCore.QSize(800, 480))
        self.setCentralWidget(self.container)

        bar_rain = BarRainfall()
        temp_hum = TempHumidity()
        time_info = TimeInfo()
        wind_dir = WindDirection()
        self.sat_image = QtWidgets.QLabel()

        layout.addWidget(temp_hum, 0, 0)
        layout.addWidget(self.sat_image, 1, 0)
        layout.addWidget(wind_dir, 0, 1)
        layout.addWidget(bar_rain, 1, 1)
        layout.addWidget(time_info, 1, 2)

        self.container.setLayout(layout)

        self.update_sat_image()

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
