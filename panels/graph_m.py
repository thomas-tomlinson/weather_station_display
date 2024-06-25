from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QPainter, QPolygon, QFont, QFontMetrics, QPen, QColor
from PyQt6.QtWidgets import QApplication
import sys
import requests
import json
import numpy as np
import pandas as pd
import weather_config.weather_config as wc
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import matplotlib.dates as mdates



class FetchData(QtCore.QObject):
    data = pyqtSignal(object)

    def __init__(self):
        QtCore.QThread.__init__(self)
        self.timer = QtCore.QTimer(self)
        self.running = True

    def start_process(self):
        self.fetch_data()
        self.timer.timeout.connect(self.fetch_data)
        # 15 minutes seems like a good starting place
        self.timer.start(900000)

    def fetch_data(self):
        try:
            alldata = pd.read_json(wc.cfg['weewx_24h_data'])
        except Exception as e:
            print("failed to retrieve graph data, reason: {}".format(e))
            return

        alldata['epochs'] = alldata['dateTime'].astype('int64') / 1000000000 
        self.data.emit(alldata)
        
    def stop(self):
        self._isRunning = False

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class Graph(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Graph, self).__init__(*args, **kwargs)
        self._data = {}
        self._data_view_current = 0
        self._data_views = [
            {'unit': 'degree F', 'title': 'Temp','series':["outTemp", "inTemp",]},
            {'unit': 'mph', 'title': 'Wind Speed', 'series':["windSpeed",]},
            {'unit': 'mph', 'title':'Wind Gust', 'series':["windGust",]},
            {'unit': 'degree F', 'title': 'Wind Chill', 'series':["windchill",]},
            {'unit': 'Humidity %', 'title': 'Humidity', 'series':["outHumidity","inHumidity"]},
            {'unit': 'inches', 'title': 'Rain', 'y_zero': True, 'series':["rain"]},
            {'unit': 'in Hg', 'title':'Barometric Pressure', 'series':["barometer"]},
            {'unit': 'voltage', 'title': 'Sensor Battery', 'series':["supplyVoltage"]},
            {'unit': 'direction', 'title':'Wind Direction', 'series':["windDir"]},
        ]
        self.sc = MplCanvas(self, width=5, height=4, dpi=100)

        self.setCentralWidget(self.sc)

        self.thread = QtCore.QThread(self)
        self.fetchdata = FetchData()
        self.fetchdata.data.connect(self.update_graph_data)
        self.fetchdata.moveToThread(self.thread)
        self.thread.started.connect(self.fetchdata.start_process)  
        self.thread.start()

    @QtCore.pyqtSlot(object)
    def update_graph_data(self, value):
        self._data = value
        self.draw_graph()

    def draw_graph(self):
        self.sc.axes.clear()
        #plot_data = self._data[['epochs', 'outTemp']].to_numpy()
        self._data.plot(x="dateTime", y="outTemp", kind="line", ax=self.sc.axes)
        self._data.plot(x="dateTime", y="inTemp", kind="line", ax=self.sc.axes)
        #self.sc.axes.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
        #self.sc.axes.plot(plot_data)
        self.sc.draw()

#    def mousePressEvent(self, event):
#        # increment our view counter
#        if self._data_view_current  == len(self._data_views) - 1:
#            self._data_view_current = 0
#        else:
#            self._data_view_current += 1 
#        #self.graph.clear()
#        self.draw_graph()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    example = Graph()
    example.show()
    app.exec()