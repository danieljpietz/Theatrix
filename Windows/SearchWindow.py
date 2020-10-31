from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QLineEdit, QListWidget
from PyQt5.QtGui import QPalette, QPainter, QBrush, QPen, QColor, QLinearGradient
from PyQt5.QtCore import Qt, QRect

import numpy as np



class SearchWindow(QtWidgets.QWidget):
    def __init__(self, steps = 0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bannerColor = [127, 127, 127, 127]
        self.brushColor = [10, 10, 10, 200]
        self.initWidth = 400
        self.initHeight = 400
        self.width = self.initWidth
        self.height = self.initHeight
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(self.width - 40, 30)
        self.textbox.setStyleSheet("color: rgb(255, 255, 255);")
        self.cb = QListWidget()
        self.cb.move(20,60)
        self.cb.insertItem(0, "Red")
        self.cb.insertItem(1, "Orange")
        self.cb.insertItem(2, "Blue")
        self.cb.setParent(self)




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
