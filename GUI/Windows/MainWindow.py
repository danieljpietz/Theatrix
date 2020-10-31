##
## This is the file for the main window
## All main window stuff goes here
##

from PyQt5.QtWidgets import QMainWindow, QGridLayout
from PyQt5.QtGui import QPainterPath
from PyQt5.QtCore import QPoint


from GUI.Windows.SearchWindow import *
from GUI.Widgets.Brick import *

from GUI.Widgets.Fixture import *
from GUI.Widgets.Functions import *
from GUI.Widgets.Inputs import *
import numpy as np


class GraphicsScene(QtWidgets.QGraphicsScene):
    def __init__(self, parent=None):
        super(GraphicsScene, self).__init__(parent)
        self.setSceneRect(0, 0, 2560,1343)


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

        painter.setPen(QPen(QColor(majorGridColor[0], majorGridColor[1], majorGridColor[2], majorGridColor[3]),  2, Qt.SolidLine))

        for i in range(0, lineCount):
            painter.drawLine(majorGridSpacing*minorGridSpacing*i, 0, majorGridSpacing*minorGridSpacing*i, lineLength)
            painter.drawLine(0, majorGridSpacing*minorGridSpacing*i, lineLength, majorGridSpacing*minorGridSpacing*i)




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

        b1 = Fixture()
        b1.setParentWindow(self)
        b1.setParent(self)
        #b1.move(event.pos().x() - b1.width / 2, event.pos().y() - np.sqrt(b1.height))
        b1.move(400 - b1.width / 2, 400 - np.sqrt(b1.height))
        b1.show()

        b1 = BrickSine()
        b1.setParentWindow(self)
        b1.setParent(self)
        # b1.move(event.pos().x() - b1.width / 2, event.pos().y() - np.sqrt(b1.height))
        b1.move(200 - b1.width / 2, 400 - np.sqrt(b1.height))
        b1.show()

        b1 = BrickTime()
        b1.setParentWindow(self)
        b1.setParent(self)
        # b1.move(event.pos().x() - b1.width / 2, event.pos().y() - np.sqrt(b1.height))
        b1.move(100 - b1.width / 2, 400 - np.sqrt(b1.height))
        b1.show()

        self.bricks.append(b1)

        pass

    def mousePressEvent(self, event):
        if self.searchWindowIsOpen:
            self.hideSearchWindow()

    def mouseDoubleClickEvent(self, event):

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

        painter.setPen(
            QPen(QColor(majorGridColor[0], majorGridColor[1], majorGridColor[2], majorGridColor[3]), 2, Qt.SolidLine))

        for i in range(0, lineCount):
            painter.drawLine(majorGridSpacing*minorGridSpacing*i, 0, majorGridSpacing*minorGridSpacing*i, lineLength)
            painter.drawLine(0, majorGridSpacing*minorGridSpacing*i, lineLength, majorGridSpacing*minorGridSpacing*i)


        painter.setPen(
            QPen(QColor(255,255,255), 2, Qt.SolidLine))
        painter.setRenderHint(QPainter.Antialiasing)
        if(self.mouseIsHot):
            mousePos = self.mapFromGlobal(QtGui.QCursor.pos())
            hotPortLoc = self.hotPort.parent.pos() +  self.hotPort.pos() + QPoint(self.hotPort.width/2, self.hotPort.height/2)
            path = QPainterPath()
            path.moveTo(hotPortLoc)
            ##TODO CUBIC PATH
            #path.cubicTo(hotPortLoc.x(),hotPortLoc.y() - 10, 0, mousePos.y() + 10, mousePos.x(), mousePos.y())
            painter.drawPath(path)
            painter.drawLine(hotPortLoc.x(), hotPortLoc.y(), mousePos.x(), mousePos.y())


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            if self.searchWindowIsOpen:
                self.hideSearchWindow()
            else:
                self.launchSearchWindow(self.mapFromGlobal(QtGui.QCursor.pos()))