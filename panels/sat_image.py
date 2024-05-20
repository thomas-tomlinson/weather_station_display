from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QPainter, QPolygon, QFont, QFontMetrics, QPen, QColor, QImage, QPixmap
from PyQt6.QtWidgets import QApplication
import sys, requests


class ImageFetch(QtCore.QObject):
    image = pyqtSignal(QPixmap) 

    def __init__(self):
        QtCore.QThread.__init__(self)
        self.timer = QtCore.QTimer(self)
        self.running = True
        self.image_list = [
            'https://cdn.star.nesdis.noaa.gov/GOES18/ABI/SECTOR/pnw/GEOCOLOR/300x300.jpg',
            'https://cdn.star.nesdis.noaa.gov/GOES18/ABI/SECTOR/pnw/AirMass/300x300.jpg',
            'https://cdn.star.nesdis.noaa.gov/GOES18/ABI/SECTOR/pnw/DayNightCloudMicroCombo/300x300.jpg',
            'https://cdn.star.nesdis.noaa.gov/GOES18/ABI/SECTOR/pnw/FireTemperature/300x300.jpg',
            'https://cdn.star.nesdis.noaa.gov/GOES18/ABI/SECTOR/pnw/Sandwich/300x300.jpg',
        ]
        self.image_position = 0

    def touch_screen_cycle(self):
        if self.image_position  == len(self.image_list) - 1:
            self.image_position = 0
        else:
            self.image_position += 1 
        self.fetch_sat_image()

    def start_process(self):
        self.fetch_sat_image()
        self.timer.timeout.connect(self.fetch_sat_image)
        # 15 minutes seems like a good starting place
        self.timer.start(900000)

    def fetch_sat_image(self):
        image = QImage()
        try:
            sat_image_bitmap = requests.get(self.image_list[self.image_position]).content
        except Exception as e:
            sat_image_bitmap = None
            print('failed to retrieve satellite image, error:', e)
        if sat_image_bitmap is not None:
            image.loadFromData(sat_image_bitmap)

        self.image.emit(QPixmap(image))
        
    def stop(self):
        self._isRunning = False

class SatImage(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(SatImage, self).__init__(*args, **kwargs)

        self._sat_image = QtWidgets.QLabel()
        self._sat_image.setScaledContents(True) 
        self.setCentralWidget(self._sat_image)

        self.thread = QtCore.QThread(self)
        self.fetchdata = ImageFetch()
        self.fetchdata.image.connect(self.update_sat_image)
        self.fetchdata.moveToThread(self.thread)
        self.thread.started.connect(self.fetchdata.start_process)  
        self.thread.start()

    @QtCore.pyqtSlot(QPixmap)
    def update_sat_image(self, image):
        self._sat_image.setPixmap(QPixmap(image))

    def mousePressEvent(self, event):
        self.fetchdata.touch_screen_cycle()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    satimage = SatImage()
    satimage.show()
    app.exec()