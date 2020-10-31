from PyQt5 import QtWidgets
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor
from PyQt5.QtCore import Qt


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
        pass

    def mouseReleaseEvent(self,event):
        self.parent.parentWindow.mouseIsHot = False
        self.parent.parentWindow.hotPort = None
        pass

    def mouseMoveEvent(self,event):
        self.parent.parentWindow.hotMousePosition = event.pos() + self.pos()
        self.parent.parentWindow.repaint()
        pass
