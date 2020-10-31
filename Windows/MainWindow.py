##
## This is the file for the main window
## All main window stuff goes here
##

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QScrollArea, QWidget, QGridLayout, QPushButton
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor
from PyQt5.QtCore import Qt, QEvent

from Widgets.widgets import *
from Windows.SearchWindow import *
import numpy as np

class GraphicsScene(QtWidgets.QGraphicsScene):
    def __init__(self, parent=None):
        super(GraphicsScene, self).__init__(parent)
        self.setSceneRect(0, 0, 2560,1343)
        pass

    def drawBackground(self, painter, rect):
        minorGridSpacing = 25
        lineLength = 10000
        lineCount = 100
        majorGridSpacing = 8
        minorGridColor = [100, 100, 100, 100]
        majorGridColor = [0, 0, 0, 255]

        ## Draw grid background
        painter.setPen(QPen(QColor(minorGridColor[0], minorGridColor[1], minorGridColor[2], minorGridColor[3]),  1, Qt.SolidLine))
        ##TODO: This is hapazard with the line distances. Probably should be fixed
        for i in range(0, lineCount):
            painter.drawLine(minorGridSpacing*i, 0, minorGridSpacing*i, lineLength)
            painter.drawLine(0, minorGridSpacing*i, lineLength, minorGridSpacing*i)
        pass
        painter.setPen(QPen(QColor(majorGridColor[0], majorGridColor[1], majorGridColor[2], majorGridColor[3]),  2, Qt.SolidLine))

        for i in range(0, lineCount):
            painter.drawLine(majorGridSpacing*minorGridSpacing*i, 0, majorGridSpacing*minorGridSpacing*i, lineLength)
            painter.drawLine(0, majorGridSpacing*minorGridSpacing*i, lineLength, majorGridSpacing*minorGridSpacing*i)
            pass



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.layout = QGridLayout()
        self.setStyleSheet("background-color: #1b1c1b;")
        self.setWindowTitle("Theatrix")
        self.scene = GraphicsScene(self)
        self.view = QtWidgets.QGraphicsView()
        self.view.setScene(self.scene)
        self.view.resize(self.scene.width(), self.scene.height())
        #self.setCentralWidget(self.view)
        self.showMaximized()

        self.searchWindow = SearchWindow()
        self.searchWindow.setParent(self)
        self.searchWindowIsOpen = False
        self.bricks = []
        self.hotMousePosition = []
        self.mouseIsHot = False
        self.hotPort = []

        pass

    def mousePressEvent(self, event):
        if self.searchWindowIsOpen:
            self.hideSearchWindow()

    def mouseDoubleClickEvent(self, event):
        """
        b1 = Brick()
        b1.setParentWindow(self)
        b1.setParent(self)
        b1.move(event.pos().x() - b1.width/2,event.pos().y() - np.sqrt(b1.height))
        b1.show()
        self.bricks.append(b1)
        """

        if not self.searchWindowIsOpen:
            self.launchSearchWindow(event.pos())
        else:
            self.searchWindow.move(event.pos().x() - self.searchWindow.width / 2, event.pos().y() - self.searchWindow.height/2)

    def launchSearchWindow(self, pos):
        self.searchWindowIsOpen = True
        self.searchWindow.move(pos.x() - self.searchWindow.width / 2, pos.y() - self.searchWindow.height/2)
        self.searchWindow.show()
        pass

    def hideSearchWindow(self):
        self.searchWindowIsOpen = False
        self.searchWindow.hide()

    def mouseMoveEvent(self, event):
        pass


    def mouseReleaseEvent(self, event):
        pass

    def paintEvent(self, event):
        ## Draw Background Grid
        minorGridSpacing = 25
        lineLength = 10000
        lineCount = 100
        majorGridSpacing = 8
        minorGridColor = [100, 100, 100, 100]
        majorGridColor = [0, 0, 0, 255]

        ## Draw grid background
        painter = QPainter(self)
        painter.setPen(QPen(QColor(minorGridColor[0], minorGridColor[1], minorGridColor[2], minorGridColor[3]),  1, Qt.SolidLine))
        ##TODO: This is hapazard with the line distances. Probably should be fixed
        for i in range(0, lineCount):
            painter.drawLine(minorGridSpacing*i, 0, minorGridSpacing*i, lineLength)
            painter.drawLine(0, minorGridSpacing*i, lineLength, minorGridSpacing*i)
        pass
        painter.setPen(QPen(QColor(majorGridColor[0], majorGridColor[1], majorGridColor[2], majorGridColor[3]),  2, Qt.SolidLine))

        for i in range(0, lineCount):
            painter.drawLine(majorGridSpacing*minorGridSpacing*i, 0, majorGridSpacing*minorGridSpacing*i, lineLength)
            painter.drawLine(0, majorGridSpacing*minorGridSpacing*i, lineLength, majorGridSpacing*minorGridSpacing*i)
            pass

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            if self.searchWindowIsOpen:
                self.hideSearchWindow()
            else:
                self.launchSearchWindow(self.mapFromGlobal(QtGui.QCursor.pos()))