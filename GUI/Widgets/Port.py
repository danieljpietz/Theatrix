from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor


class Port(QtWidgets.QWidget):
    def __init__(self, steps=1, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.height = 15
        self.width = 15
        self.resize(self.width, self.height)
        self.isConnected = False;
        self.portType = None
        self.connections = []
        self.value = None

    def setParentBrick(self, parent):
        self.parent = parent

    def getValue(self):
        if self.parent.updateID == self.parent.parentWindow.updateID:
            return self.value
        else:
            self.updateValue()
            return self.value

    def updateValue(self):
        if self.portType == "Input":
            if len(self.connections) == 0:
                self.value = 0
                return
            else:
                self.value = self.connections[0].getValue()
                return
        else:
            self.parent.eval()

    def paintEvent(self, event):

        penColor = [200, 200, 200, 200]

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing);
        painter.setPen(QPen(QColor(penColor[0], penColor[1], penColor[2], penColor[3]), 3, Qt.SolidLine))
        if self.isConnected:
            painter.setBrush(QBrush(QColor(penColor[0], penColor[1], penColor[2], penColor[3]), Qt.SolidPattern))
            pass
        painter.drawEllipse(0, 0, self.width, self.height)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.parent.parentWindow.mouseIsHot = True
            self.parent.parentWindow.hotPort = self
        elif event.button() == Qt.RightButton:
            self.disconnectAll()
        pass

    def mouseReleaseEvent(self, event):
        self.parent.parentWindow.mouseIsHot = False
        self.parent.parentWindow.hotPort = None
        self.parent.parentWindow.connectionManager.tryConnect(self, event.pos())
        self.parent.parentWindow.repaint()
        pass

    def mouseMoveEvent(self, event):
        self.parent.parentWindow.hotMousePosition = event.pos() + self.pos()
        self.parent.parentWindow.repaint()
        pass

    def disconnectAll(self):
        for port in self.connections:
            self.disconnect(port)

    def disconnect(self, port):
        port.connections.remove(self)
        self.connections.remove(port)
        if len(self.connections) == 0:
            self.isConnected = False
        if len(port.connections) == 0:
            port.isConnected = False

    def isConnectedTo(self, port):
        for p in self.connections:
            if p == port:
                return True
        return False
