from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QPolygon, QFont, QFontMetrics, QPen, QColor
from PyQt6.QtWidgets import QApplication
import pyqtgraph as pg 
import sys
import requests
import json
import numpy as np

class Graph(QtWidgets.QMainWindow):
    _data = {}
    def __init__(self, *args, **kwargs):
        super(Graph, self).__init__(*args, **kwargs)
        self._data = []
        self._data_view_current = 0
        self.plot_graph = pg.PlotWidget()
        self.setCentralWidget(self.plot_graph) 

        self.fetch_data()
        self.draw_graph()

    def draw_graph(self):
        series = self._data_view_current
        pen = pg.mkPen(color=(255, 0, 0))
        axis = pg.DateAxisItem()
        self.plot_graph.setLabel("left", self._data[series]['y_axis_label'])
        self.plot_graph.setLabel("bottom", "Time")
        self.plot_graph.setAxisItems({'bottom':axis})
        #print("x_axis:", len(self._data[series]['x_axis']))
        #print("y_axis:", len(self._data[series]['y_axis']))
        #self.graph = self.plot_graph.plot(self._data[series]['x_axis'], self._data[series]['y_axis'], pen=pen)
        self.graph = self.plot_graph.plot(self._data[series]['plot_data'], pen=pen, connect='finite')

    def mousePressEvent(self, event):
        # increment our view counter
        if self._data_view_current  == len(self._data) - 1:
            self._data_view_current = 0
        else:
            self._data_view_current += 1 
        self.graph.clear()
        self.draw_graph()

    def fetch_data(self):
        holder = []
        # remove all data
        self._data = []
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
                self._data.append(temp_object)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    example = Graph()
    example.show()
    app.exec()