from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt


class SearchListEntry(QtWidgets.QWidget):
    def __init__(self, steps = 1, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.height = 20
        self.width = 200
        self.resize(self.width,self.height)

    def sizeHint(self):
        return QtCore.QSize(self.width, self.height)
    def paintEvent(self, event):

        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 5, Qt.DotLine))
        painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
        painter.drawRect(0, 0, self.width, self.height)


