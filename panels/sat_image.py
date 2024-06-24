from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QPainter, QPolygon, QFont, QFontMetrics, QPen, QColor, QImage, QPixmap
from PyQt6.QtWidgets import QApplication
import sys, requests
import weather_config.weather_config as wc

class ImageFetch(QtCore.QObject):
    image = pyqtSignal(QPixmap) 

    def __init__(self):
        QtCore.QThread.__init__(self)
        self.timer = QtCore.QTimer(self)
        self.running = True
        self.image_list = wc.cfg['sat_images']
        self.image_position = 0
        self.image_holder = []

    def touch_screen_cycle(self):
        if len(self.image_list) == 1:
            # only a single image, nothing to do here
            return

        if self.image_position  == len(self.image_list) - 1:
            self.image_position = 0
        else:
            self.image_position += 1 
        self.image.emit(self.image_holder[self.image_position])
        #self.fetch_sat_image()

    def start_process(self):
        self.fetch_all_images()
        self.timer.timeout.connect(self.fetch_all_images)
        # 15 minutes seems like a good starting place
        self.timer.start(900000)

    def fetch_all_images(self):
        #clear the current images
        self.image_holder = []
        #retrieve all of the sat images and store them for use.
        for entry in self.image_list:
            image = QImage()
            try:
                sat_image_bitmap = requests.get(entry).content
            except Exception as e:
                sat_image_bitmap = None
                print('failed to retrieve satellite image, error:', e)
                next
            if sat_image_bitmap is not None:
                image.loadFromData(sat_image_bitmap)
            #scale the image to 300x300
            qp = QPixmap(image)
            qp_scaled = qp.scaled(300,300)
            #self.image.emit(QPixmap(image))
            self.image_holder.append(qp_scaled)
        # emit the current offset image
        self.image.emit(self.image_holder[self.image_position])  
        
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
        self._last = "Click"

    def mouseReleaseEvent(self, event):
        if self._last == "Click":
            QtCore.QTimer.singleShot(QApplication.instance().doubleClickInterval(),
                                     self.performSingleClickAction)
        else:
            pass
            #self.message = "Double Click"
            #self.update()

    def mouseDoubleClickEvent(self, event):
        self._last = "Double Click" 

    def performSingleClickAction(self):
        if self._last == "Click":
            self.fetchdata.touch_screen_cycle()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    satimage = SatImage()
    satimage.show()
    app.exec()