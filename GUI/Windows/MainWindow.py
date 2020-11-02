##
## This is the file for the main window
## All main window stuff goes here
##
from PyQt5.QtCore import QRect, QSize
from PyQt5.QtGui import QPainterPath
from PyQt5.QtWidgets import QMainWindow, QGridLayout


from GUI.Windows.ConnectionHandler import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.layout = QGridLayout()
        self.setStyleSheet("background-color: #1b1c1b;")
        self.setWindowTitle("Theatrix")
        self.showMaximized()

        self.searchWindow = SearchWindow()
        self.searchWindow.setParent(self)
        self.searchWindowIsOpen = False
        self.searchWindow.mainWindow = self
        self.bricks = []
        self.hotMousePosition = []
        self.mouseIsHot = False
        self.hotPort = []

        self.shiftIsDown = False

        self.shouldDrawSelectionBox = False

        self.connectionManager = ConnectionHandler()
        self.connectionManager.setParent(self)
        self.connectionManager.setParentWindow(self)
        self.connectionManager.show()

        self.selectedBricks = []
        self.boxedRects = []

        self.updateID = 0
        self.updateManager = None
        self.outputBricks = []
        self.copyBuffer = []

        self.addBrick(Fixture, QPoint(400, 400))
        self.addBrick(BrickTime, QPoint(200, 200))

        pass

    def updateDMX(self):
        for brick in self.outputBricks:
            brick.eval()

    def addBrick(self, brickClass, pos):
        brick = brickClass()
        brick.setParentWindow(self)
        brick.setParent(self)
        brick.move(pos.x(), pos.y())
        self.bricks.append(brick)
        self.connectionManager.addBrick(brick)
        if brick.isOutput:
            self.outputBricks.append(brick)
        brick.show()

    def addToSelected(self, brick):
        if not self.isSelected(brick):
            brick.isSelected = True
            self.selectedBricks.append(brick)

    def clearSelected(self):
        for b in self.selectedBricks:
            b.update()
            b.isSelected = False

        self.selectedBricks = []

    def deselect(self, brick):
        brick.isSelected = False
        brick.update()
        self.selectedBricks.remove(brick)

    def isSelected(self, brick):
        for b in self.selectedBricks:
            if b == brick:
                return True
        return False

    def copySelected(self):
        self.copyBuffer = []
        for b in self.selectedBricks:
            print([Bricktionary[type(b)], b.mapToParent(b.pos())])

    def pasteSelected(self):
        for brick in self.copyBuffer:
            self.addBrick(type(brick), brick.pos())

    def deleteSelected(self):
        for brick in self.selectedBricks:
            for port in brick.inputPorts + brick.outputPorts:
                port.disconnectAll()
        self.update()

    def mousePressEvent(self, event):
        self.mousePressLocation = event.pos()
        self.boxedRects = []
        if QApplication.keyboardModifiers() != Qt.ShiftModifier:
            self.clearSelected()
        if self.searchWindowIsOpen:
            self.hideSearchWindow()

    def mouseMoveEvent(self, event):
        self.mouseDragLocation = event.pos()
        self.shouldDrawSelectionBox = True
        self.repaint()

    def mouseDoubleClickEvent(self, event):
        if not self.searchWindowIsOpen:
            self.launchSearchWindow(event.pos())
        else:
            self.searchWindow.move(event.pos().x() - self.searchWindow.width / 2,
                                   event.pos().y() - self.searchWindow.height / 2)

    def launchSearchWindow(self, pos):
        self.searchWindowIsOpen = True
        self.searchWindow.move(pos.x() - self.searchWindow.width / 2, pos.y() - self.searchWindow.height / 2)
        self.searchWindow.show()
        self.searchWindow.raise_()

    def hideSearchWindow(self):
        self.searchWindowIsOpen = False
        self.searchWindow.hide()

    def mouseReleaseEvent(self, event):
        self.shouldDrawSelectionBox = False
        self.boxedRects = []
        self.repaint()
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
        painter.setPen(
            QPen(QColor(minorGridColor[0], minorGridColor[1], minorGridColor[2], minorGridColor[3]), 1, Qt.SolidLine))
        ##TODO: This is hapazard with the line distances. Probably should be fixed
        for i in range(0, lineCount):
            painter.drawLine(minorGridSpacing * i, 0, minorGridSpacing * i, lineLength)
            painter.drawLine(0, minorGridSpacing * i, lineLength, minorGridSpacing * i)

        painter.setPen(
            QPen(QColor(majorGridColor[0], majorGridColor[1], majorGridColor[2], majorGridColor[3]), 2, Qt.SolidLine))

        for i in range(0, lineCount):
            painter.drawLine(majorGridSpacing * minorGridSpacing * i, 0, majorGridSpacing * minorGridSpacing * i,
                             lineLength)
            painter.drawLine(0, majorGridSpacing * minorGridSpacing * i, lineLength,
                             majorGridSpacing * minorGridSpacing * i)

        painter.setPen(
            QPen(QColor(255, 255, 255), 2, Qt.SolidLine))
        painter.setRenderHint(QPainter.Antialiasing)
        cubicCurveFactor = 0.5
        if (self.mouseIsHot):
            mousePos = self.mapFromGlobal(QtGui.QCursor.pos())
            hotPortLoc = self.hotPort.parent.pos() + self.hotPort.pos() + QPoint(self.hotPort.width / 2,
                                                                                 self.hotPort.height / 2)
            path = QPainterPath()
            path.moveTo(hotPortLoc)
            ##TODO CUBIC PATH
            path.cubicTo(hotPortLoc + QPoint((mousePos.x() - hotPortLoc.x()) * cubicCurveFactor, 0),
                         mousePos - QPoint((mousePos.x() - hotPortLoc.x()) * cubicCurveFactor, 0), mousePos)

            painter.drawPath(path)
            # painter.drawLine(hotPortLoc.x(), hotPortLoc.y(), mousePos.x(), mousePos.y())

        for input in self.connectionManager.inputPorts:
            for connection in input.connections:
                painter.setPen(QPen(QColor(255, 255, 255), 2, Qt.SolidLine))
                painter.setRenderHint(QPainter.Antialiasing)
                port1Pos = input.parent.mapToParent(input.pos()) + QPoint(
                    input.size().width(), input.size().height()) / 2 - 0 * QPoint(self.size().width(), 0)
                port2Pos = connection.parent.mapToParent(connection.pos()) + QPoint(
                    connection.size().width(), connection.size().height()) / 2 - 0 * QPoint(self.size().width(), 0)
                path = QPainterPath()
                path.moveTo(port1Pos)
                ##TODO CUBIC PATH
                path.cubicTo(port1Pos - QPoint((port1Pos.x() - port2Pos.x()) * cubicCurveFactor, 0),
                             port2Pos + QPoint((port1Pos.x() - port2Pos.x()) * cubicCurveFactor, 0), port2Pos)
                painter.drawPath(path)

        if self.shouldDrawSelectionBox:
            painter.setPen(QPen(QColor(255, 255, 255), 1, Qt.DashLine))
            selectionRect = QRect(np.min([self.mousePressLocation.x(), self.mouseDragLocation.x()]),
                                  np.min([self.mousePressLocation.y(), self.mouseDragLocation.y()]),
                                  np.abs(self.mousePressLocation.x() - self.mouseDragLocation.x()),
                                  np.abs(self.mousePressLocation.y() - self.mouseDragLocation.y()))
            painter.drawRect(selectionRect)

            for brick in self.bricks:
                P1 = brick.rect().topLeft()
                brickRect = QRect(brick.mapTo(self, P1),
                                  QSize(brick.rect().size().width(), brick.rect().size().height()))
                if selectionRect.intersects(brickRect):
                    self.addToSelected(brick)
                    if brick not in self.boxedRects:
                        self.boxedRects.append(brick)
                else:
                    if brick in self.boxedRects:
                        self.deselect(brick)
                        self.boxedRects.remove(brick)

    def keyPressEvent(self, event):
        if event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_C:
            self.copySelected()
        elif event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_A:
            for b in self.bricks:
                self.addToSelected(b)
                b.update()
        elif event.key() == Qt.Key_Space:
            if self.searchWindowIsOpen:
                self.hideSearchWindow()
            else:
                self.launchSearchWindow(self.mapFromGlobal(QtGui.QCursor.pos()))
        elif event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_V:
            self.pasteSelected()
        elif event.key() == Qt.Key_Delete or event.key() == Qt.Key_Backspace:
            print("Del")
            self.deleteSelected()
