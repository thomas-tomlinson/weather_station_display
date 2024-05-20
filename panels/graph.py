from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QPainter, QPolygon, QFont, QFontMetrics, QPen, QColor
from PyQt6.QtWidgets import QApplication
import pyqtgraph as pg 
import sys
import requests
import json
import numpy as np

class FetchData(QtCore.QObject):
    data = pyqtSignal(list)

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
        holder = []
        # remove all data
        return_data = [] 
        raw_data = requests.get('http://weewx01.localdomain/belchertown/json/day.json')
        json_data = json.loads(raw_data.content)        
        for keys in json_data:
            if keys.startswith('chart') is True and isinstance(json_data[keys], dict):
                holder.append(json_data[keys])

        for entry in holder:
            for charttype in entry['series']:
                temp_object = {}
                temp_object['name'] = entry['series'][charttype]['name']
                temp_object['y_axis_label'] = entry['series'][charttype]['yAxis_label']
                a = np.array(entry['series'][charttype]['data'], np.float32)
                a[:,0] = a[:,0] / 1000 
                temp_object['plot_data'] = a
                return_data.append(temp_object)
        self.data.emit(return_data)
        
    def stop(self):
        self._isRunning = False

class Graph(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Graph, self).__init__(*args, **kwargs)
        self._data = []
        self._data_view_current = 0
        self.plot_graph = pg.PlotWidget()
        self.plot_graph.setMouseEnabled(x=False, y=False)
        self.setCentralWidget(self.plot_graph) 

        self.thread = QtCore.QThread(self)
        self.fetchdata = FetchData()
        self.fetchdata.data.connect(self.update_graph_data)
        self.fetchdata.moveToThread(self.thread)
        self.thread.started.connect(self.fetchdata.start_process)  
        self.thread.start()

    @QtCore.pyqtSlot(list)
    def update_graph_data(self, value):
        self._data = value
        self.draw_graph()

    def draw_graph(self):
        series = self._data_view_current
        pen = pg.mkPen(color=(255, 0, 0))
        axis = pg.DateAxisItem()
        self.plot_graph.clear()
        self.plot_graph.setLabel("left", self._data[series]['y_axis_label'])
        self.plot_graph.setLabel("bottom", "Time")
        self.plot_graph.setAxisItems({'bottom':axis})
        graph = self.plot_graph.plot(self._data[series]['plot_data'], pen=pen, connect='finite')

    def mousePressEvent(self, event):
        # increment our view counter
        if self._data_view_current  == len(self._data) - 1:
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