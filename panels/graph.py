from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QPainter, QPolygon, QFont, QFontMetrics, QPen, QColor
from PyQt6.QtWidgets import QApplication
import pyqtgraph as pg 
import sys
import requests
import json
import numpy as np
import pandas as pd
import weather_config.weather_config as wc

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
        alldata = pd.read_json(wc.cfg['weewx_24h_data'])
        #alldata.set_index('dateTime', inplace=True) 
        alldata['epochs'] = alldata['dateTime'].astype('int64') / 1000000000 
        self.data.emit(alldata)
        
    def stop(self):
        self._isRunning = False

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
        self._pens = [
            pg.mkPen(color=(255, 0, 0)),
            pg.mkPen(color=(0, 255, 0)),
        ]
        self.plot_graph = pg.PlotWidget()
        self.plot_graph.setMouseEnabled(x=False, y=False)
        self.plot_graph.setObjectName("graph")
        self.setCentralWidget(self.plot_graph) 

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
        data_view = self._data_views[self._data_view_current]
        axis = pg.DateAxisItem()
        self.plot_graph.clear()
        self.plot_graph.addLegend(offset=1, colCount=2)
        self.plot_graph.setLabel("left", data_view['unit'])
        self.plot_graph.setLabel("bottom", "Time")
        self.plot_graph.setAxisItems({'bottom':axis})
        self.plot_graph.setTitle(data_view['title'])
        if 'y_zero' in data_view:
            if data_view['y_zero'] is True:
                self.plot_graph.setYRange(0, 5)
        else:
            self.plot_graph.enableAutoRange(y=True)
        pen_counter = 0
        for dtype in data_view['series']:
            plotdata = np.array(self._data[['epochs',dtype]])
            graph = self.plot_graph.plot(plotdata, pen=self._pens[pen_counter], connect='finite', name=dtype)
            pen_counter += 1

    def mousePressEvent(self, event):
        # increment our view counter
        if self._data_view_current  == len(self._data_views) - 1:
            self._data_view_current = 0
        else:
            self._data_view_current += 1 
        #self.graph.clear()
        self.draw_graph()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    example = Graph()
    example.show()
    app.exec()