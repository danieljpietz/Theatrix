from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPalette, QPainter, QBrush, QPen, QColor, QLinearGradient
from PyQt5.QtCore import Qt, QRect

from Widgets.widgets import *

import numpy as np


class Port(QtWidgets.QWidget):
    def __init__(self, steps = 1, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.height = 15
        self.width = 15
        self.resize(self.width,self.height)
        self.isConnected = False;

    def setParentBrick(self, parent):
        self.parent = parent

    def paintEvent(self, event):

        penColor = [200, 200, 200, 200]

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing);
        painter.setPen(QPen(QColor(penColor[0], penColor[1], penColor[2], penColor[3]),  3, Qt.SolidLine))
        if self.isConnected == True:
            painter.setBrush(QBrush(QColor(penColor[0], penColor[1], penColor[2], penColor[3]), Qt.SolidPattern))
            pass
        painter.drawEllipse(0, 0, self.width,self.height)


    def mousePressEvent(self,event):
        self.parent.parentWindow.mouseIsHot = True
        self.parent.parentWindow.hotPort = self
        print("HOT")
        pass

    def mouseReleaseEvent(self,event):
        self.parent.parentWindow.mouseIsHot = False
        self.parent.parentWindow.hotPort = None
        print("Not HOT")
        pass

    def mouseMoveEvent(self,event):
        self.parent.parentWindow.hotMousePosition = event.pos() + self.pos()
        pass
