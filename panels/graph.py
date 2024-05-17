from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QPolygon, QFont, QFontMetrics, QPen, QColor
from PyQt6.QtWidgets import QApplication
import pyqtgraph as pg 
import sys
import requests
import json

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
        self.plot_graph.setLabel("left", self._data[series]['y_axis_label'])
        self.plot_graph.setLabel("bottom", "Time")
        self.graph = self.plot_graph.plot(self._data[series]['x_axis'], self._data[series]['y_axis'], pen=pen)

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
        raw_data = requests.get('http://wdisplay01.local/weewx/belchertown/json/day.json')
        json_data = json.loads(raw_data.content)        
        for keys in json_data:
            if keys.startswith('chart') is True and isinstance(json_data[keys], dict):
                holder.append(json_data[keys])

        for entry in holder:
            for charttype in entry['series']:
                temp_object = {}
                temp_object['name'] = entry['series'][charttype]['name']
                temp_object['y_axis_label'] = entry['series'][charttype]['yAxis_label']
                temp_object['x_axis'] = []
                temp_object['y_axis'] = []
                for value in entry['series'][charttype]['data']:
                    temp_object['x_axis'].append(value[0])
                    temp_object['y_axis'].append(value[1])
                self._data.append(temp_object)






if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    example = Graph()
    example.show()
    app.exec()