from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel, QApplication
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor, QLinearGradient
from PyQt5.QtCore import Qt

from GUI.Widgets.Port import Port

import numpy as np


class Brick(QtWidgets.QWidget):
    def __init__(self, steps = 0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bannerColor = [255, 255, 255, 200]
        self.brushColor = [10, 10, 10, 200]
        self.penColor = [200, 200, 200, 200]
        self.selectedColor = [255, 180, 3, 200]
        self.initWidth = 400
        self.initHeight = 400
        self.width = self.initWidth
        self.height = self.initHeight
        self.isSelected = False
        self.setupTitle("Brick")
        self.setInputs([])
        self.setOutputs([])
        self.addPorts()

    def setInputs(self, inputs):
        self.inputs = inputs
        self.inputCount = len(self.inputs)
        self.inputPorts = []


    def setOutputs(self, outputs):
        self.outputs = outputs
        self.outputCount = len(self.outputs)
        self.outputPorts = []


    def setupTitle(self, title):
        self.title = title
        self.titleLabel = QLabel(self.title)
        self.titleLabel.setParent(self)
        self.titleLabel.move(4, 4)
        self.titleLabel.setStyleSheet("color: rgb(255, 255, 255); background-color: rgba(0,0,0,0);")
        titleFont = QtGui.QFont()
        titleFont.setBold(True)
        self.titleLabel.setFont(titleFont)
        self.titleLabel.adjustSize()

    def setTitle(self, title):
        self.titleLabel.setText(title)
        self.titleLabel.adjustSize()

    def setParentWindow(self, window):
        self.parentWindow = window

    def addPorts(self):
        #TODO: Autosizing
        maxInputSize = 0;
        maxOutputSize = 0;
        for i in range(0, self.inputCount):
            port = Port()
            port.setParent(self)
            port.setParentBrick(self)
            port.move(0.5*port.size().width(), self.initHeight/8 + i * 1.5*(port.size().height()))
            port.portType = "Input"
            port.show()
            inputLabel = QLabel(self.inputs[i])
            inputLabel.setParent(self)
            inputLabel.move(10 + 1.5*port.size().width(), self.initHeight/8 + i * 1.5*(port.size().height()))
            inputLabel.adjustSize()
            inputLabel.setStyleSheet("color: rgb(255, 255, 255); background-color: rgba(0,0,0,0);")
            self.inputPorts.append(port)
            if inputLabel.width() > maxInputSize:
                maxInputSize = inputLabel.width()
                pass

            pass

        for i in range(0, self.outputCount):
            port = Port()
            port.setParent(self)
            port.setParentBrick(self)
            port.move(self.initWidth - 1.5*port.size().width(), self.initHeight/8 + i * 1.5*(port.size().height()))
            port.portType = "Output"
            port.show()
            outputLabel = QLabel(self.outputs[i])
            outputLabel.setParent(self)
            outputLabel.adjustSize()
            outputLabel.move(self.initWidth - 1.5*port.size().width() - outputLabel.width() - 10, self.initHeight / 8 + i * 1.5 * (port.size().height()))
            outputLabel.setStyleSheet("color: rgb(255, 255, 255); background-color: rgba(0,0,0,0);")
            self.outputPorts.append(port)
            if outputLabel.width() > maxOutputSize:
                maxOutputSize = outputLabel.width()
                pass
            pass
        if (self.inputCount or self.outputCount) == 0:
            self.height = self.initHeight / 6
        else:
            self.height = self.initHeight / 6 + np.max([self.inputCount, self.outputCount]) * 1.5 * (
                port.size().height())
        self.resize(self.width, self.height)




    def paintEvent(self, event):

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing);
        painter.setPen(QPen(QColor(self.penColor[0], self.penColor[1], self.penColor[2], self.penColor[3]),  2, Qt.SolidLine))
        gradient = QLinearGradient(0, 0, self.width, 0)
        gradient.setColorAt(0.0, QColor(self.bannerColor[0], self.bannerColor[1], self.bannerColor[2], self.bannerColor[3]))
        gradient.setColorAt(0.85, QColor(self.brushColor[0], self.brushColor[1], self.brushColor[2], self.brushColor[3]))
        painter.setBrush(QBrush(QColor(self.brushColor[0], self.brushColor[1], self.brushColor[2], self.brushColor[3]), Qt.SolidPattern))
        #painter.setBrush(QBrush(gradient))
        painter.drawRoundedRect(0, 0, self.width, self.height, 0, np.sqrt(self.height))
        painter.setBrush(QBrush(gradient))
        painter.setPen(QPen(QColor(self.penColor[0], self.penColor[1], self.penColor[2], 0),  0, Qt.SolidLine))
        painter.drawRect(2, 2, self.width - 4, 2*np.sqrt(self.height))
        if self.isSelected:
            painter.setBrush(
                QBrush(QColor(0, 0, 0, 0),
                       Qt.SolidPattern))
            painter.setPen(
                QPen(QColor(self.selectedColor[0], self.selectedColor[1], self.selectedColor[2], self.selectedColor[3]), 2, Qt.SolidLine))
            painter.drawRect(0, 0, self.width, self.height)

    def mouseReleaeEvent(self, event):
        if QApplication.keyboardModifiers() != Qt.ShiftModifier:
            self.parent().clearSelected()
        self.parent().addToSelected(self)

    def mousePressEvent(self,event):
        self.update()
        self.lastTouch = event.pos()
        self.position = self.pos()
        if QApplication.keyboardModifiers() != Qt.ShiftModifier and len(self.parent().selectedBricks) == 1:
            self.parent().clearSelected()
        self.parent().addToSelected(self)
        pass

    def mouseMoveEvent(self,event):
        for brick in self.parent().selectedBricks:
            brick.move(brick.pos() + event.pos() - self.lastTouch)
            brick.raise_()
        self.parent().repaint()


