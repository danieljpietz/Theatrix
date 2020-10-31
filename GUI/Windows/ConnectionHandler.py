##
## This is the file for the main window
## All main window stuff goes here
##

from PyQt5.QtGui import QPainterPath
from PyQt5.QtCore import QPoint

from GUI.Windows.SearchWindow import *


class ConnectionDrawHandler(QWidget):
    def __init__(self):
        super().__init__()
        self.view.setScene(self.scene)
        self.view.resize(self.scene.width(), self.scene.height())

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