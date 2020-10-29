from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPalette, QPainter, QBrush, QPen, QColor, QLinearGradient
from PyQt5.QtCore import Qt, QRect

from Widgets.Port import Port

import numpy as np


class Brick(QtWidgets.QWidget):
    def __init__(self, steps = 0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bannerColor = [127, 127, 127, 127]
        self.brushColor = [10, 10, 10, 200]
        self.initWidth = 400
        self.initHeight = 400
        self.width = self.initWidth
        self.height = self.initHeight
        self.inputCount = 3
        self.outputCount = 3
        self.resize(self.width, self.height)
        self.inputs = []
        self.outputs = []
        self.addPorts()

    def setParentWindow(self, window):
        self.parentWindow = window

    def addPorts(self):
        for i in range(0, self.inputCount):
            port = Port()
            port.setParent(self)
            port.setParentBrick(self)
            port.move(0.5*port.size().width(), self.initHeight/8 + i * 1.5*(port.size().height()))
            port.show()
            self.inputs.append(port)
            pass

        for i in range(0, self.outputCount):
            port = Port()
            port.setParent(self)
            port.setParentBrick(self)
            port.move(self.initWidth - 1.5*port.size().width(), self.initHeight/8 + i * 1.5*(port.size().height()))
            port.show()
            self.outputs.append(port)
            pass
        self.height = self.initHeight/6 + np.max([self.inputCount, self.outputCount])*1.5*(port.size().height())



    def paintEvent(self, event):
        penColor = [200, 200, 200, 200]
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing);
        painter.setPen(QPen(QColor(penColor[0], penColor[1], penColor[2], penColor[3]),  2, Qt.SolidLine))
        gradient = QLinearGradient(0, 0, 0, self.height)
        gradient.setColorAt(0.0, QColor(self.bannerColor[0], self.bannerColor[1], self.bannerColor[2], self.bannerColor[3]))
        gradient.setColorAt(0.15, QColor(self.brushColor[0], self.brushColor[1], self.brushColor[2], self.brushColor[3]))
        painter.setBrush(QBrush(QColor(self.brushColor[0], self.brushColor[1], self.brushColor[2], self.brushColor[3]), Qt.SolidPattern))
        #painter.setBrush(QBrush(gradient))
        painter.drawRoundedRect(0, 0, self.width, self.height, np.sqrt(self.width), np.sqrt(self.height))


    def mousePressEvent(self,event):
        self.lastTouch = event.pos()
        self.position = self.pos()
        pass

    def mouseMoveEvent(self,event):
        self.move(self.pos() + event.pos() - self.lastTouch)
