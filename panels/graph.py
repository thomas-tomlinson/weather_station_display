from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QPolygon, QFont, QFontMetrics, QPen, QColor
from PyQt6.QtWidgets import QApplication
import pyqtgraph as pg 
import sys
from random import randint

class Graph(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(Graph, self).__init__(*args, **kwargs)

        self.plot_graph = pg.PlotWidget()
        self.setCentralWidget(self.plot_graph) 
        self.minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 30]
        pen = pg.mkPen(color=(255, 0, 0))
        self.plot_graph.setLabel("left", "Temp")
        self.plot_graph.setLabel("bottom", "Time")
        self.graph = self.plot_graph.plot(self.minutes, self.temperature, pen=pen)

    def mousePressEvent(self, event):
        pen = pg.mkPen(color=(randint(0, 255), randint(0, 255), randint(0, 255)))
        self.graph.setData(self.minutes, self.temperature, pen=pen)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    example = Graph()
    example.show()
    app.exec()